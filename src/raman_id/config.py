from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[2]
data_env = os.getenv("DATA_DIR")

if data_env:
    p = Path(data_env).expanduser()
    DATA_DIR = p if p.is_absolute() else (PROJECT_ROOT / p)
else:
    DATA_DIR = PROJECT_ROOT / "data"

RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"