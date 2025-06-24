import pathlib

def get_root_path() -> pathlib.WindowsPath:
    return pathlib.Path.joinpath(pathlib.Path.cwd())