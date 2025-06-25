import pathlib

SOFTWARE_DATA_FILE = (
    pathlib.Path(__file__).parent.parent.parent / "data" / "meta" / "software.yaml"
)
SERVER_DATA_FILE = (
    pathlib.Path(__file__).parent.parent.parent / "data" / "meta" / "servers.yaml"
)

SERVER_ROOT = pathlib.Path(__file__).parent.parent.parent / "data" / "servers"
