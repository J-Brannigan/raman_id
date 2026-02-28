from pathlib import Path
import os
from dotenv import load_dotenv

load_dotenv()

def find_project_root() -> Path:
    # Prefer the current working tree so notebooks still resolve repo-local data
    # even when the package is imported from an installed environment.
    candidates = [Path.cwd(), Path(__file__).resolve().parent]

    for start in candidates:
        for candidate in (start, *start.parents):
            if (candidate / "pyproject.toml").exists():
                return candidate

    return Path(__file__).resolve().parents[2]


PROJECT_ROOT = find_project_root()
data_env = os.getenv("DATA_DIR")

if data_env:
    p = Path(data_env).expanduser()
    DATA_DIR = p if p.is_absolute() else (PROJECT_ROOT / p)
else:
    DATA_DIR = PROJECT_ROOT / "data"

RAW_DIR = DATA_DIR / "raw"
INTERIM_DIR = DATA_DIR / "interim"