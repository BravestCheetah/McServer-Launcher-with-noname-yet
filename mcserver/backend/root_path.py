import pathlib

def get_root_path() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parent.parent.parent