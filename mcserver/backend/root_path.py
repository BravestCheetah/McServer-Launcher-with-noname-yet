import pathlib

def get_root_path() -> pathlib.WindowsPath:
    return pathlib.Path(__file__).resolve().parent.parent