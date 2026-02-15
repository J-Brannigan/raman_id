from pathlib import Path
import os
from raman_id.config import RAW_DIR


RAW_EXCELLENT_UNORIENTED_FOLDER = RAW_DIR / 'rruff_excellent_unoriented'

def load_rruff_file(path: Path):
    with path.open('r') as f:
        return path.name, f.readlines()

pathlist = RAW_EXCELLENT_UNORIENTED_FOLDER.rglob('Abellaite*.txt')

spectra={}
for path in pathlist:
    spectrum_name, spectrum = load_rruff_file(path)
    spectra[spectrum_name]=spectrum

print(len(spectra))