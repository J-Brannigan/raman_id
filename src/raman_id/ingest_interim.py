from pathlib import Path
from raman_id.config import RAW_DIR, INTERIM_DIR
import numpy as np
import h5py
import re
from tqdm import tqdm

RAW_EXCELLENT_UNORIENTED_FOLDER = RAW_DIR / 'rruff_excellent_unoriented'
INTERIM_EXCELLENT_UNORIENTED_FOLDER = INTERIM_DIR / 'excellent_unoriented'
print(RAW_EXCELLENT_UNORIENTED_FOLDER)

raw_file_count = sum(1 for p in RAW_EXCELLENT_UNORIENTED_FOLDER.iterdir() if p.is_file())
print(f'Number of raw file: {raw_file_count}')

def load_rruff_file(path: Path):
    with path.open('r') as f:
        return path.name, f.readlines()

def to_float_or_nan(value):
    value = value.strip()
    if value in {"", "-", "NULL"}:
        return np.nan
    try:
        return float(value)
    except ValueError:
        return np.nan

def parse_spectra(raw_spectrum_record):
    metadata= {'filename':raw_spectrum_record['filename']}
    raman_shifts=[]
    intensities=[]
    for line in raw_spectrum_record['spectrum']:
        if line.strip() == '':
            continue
        if line.startswith('#'):
            metadata[line.split('=')[0].strip("#").replace(' ','_')]=line.split('=')[1].strip('\n')
        else:
            if '\t' in line:
                line=line.replace('\t',',')
                continue
            parsed_values = re.sub(' +',',',line.strip('\n').strip().replace(',',' ').replace('\t',' ')).split(',')
            if parsed_values !=['']:

                shift = to_float_or_nan(parsed_values[0])
                intensity = to_float_or_nan(parsed_values[1])
                if np.isnan(shift):
                    continue

                raman_shifts.append(shift)
                intensities.append(intensity)
    spectral_data=np.array([raman_shifts,intensities])
    return {'metadata': metadata, 'spectral_data': spectral_data}

pathlist = RAW_EXCELLENT_UNORIENTED_FOLDER.rglob('*.txt')
for path in tqdm(pathlist,total=raw_file_count):
    try:
        spectrum_name, spectrum = load_rruff_file(path)
        parsed_spectrum = parse_spectra({"filename": spectrum_name, "spectrum": spectrum})
        with h5py.File(f'{INTERIM_EXCELLENT_UNORIENTED_FOLDER}/{spectrum_name.replace('.txt','')}.h5','w') as h5:
            grp = h5.create_group('spectra')
            s = grp.create_group(spectrum_name.replace('.txt',''))
            s.create_dataset('data', data = parsed_spectrum['spectral_data'])
            for key, value in parsed_spectrum['metadata'].items():
                s.attrs[key] = value
    except:
        print(path)

interim_file_count = sum(1 for p in INTERIM_EXCELLENT_UNORIENTED_FOLDER.iterdir() if p.is_file())

print(f'Number of raw files: {raw_file_count}')
print(f'Number of interim files: {interim_file_count}')