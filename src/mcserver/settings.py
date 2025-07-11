import pathlib

ROOT = (
    pathlib.Path(__file__).parent.parent.parent
)

SOFTWARE_DATA_FILE = (
    ROOT / "data" / "meta" / "software.yaml"
)
SERVER_DATA_FILE = (
    ROOT / "data" / "meta" / "servers.yaml"
)

SERVER_ROOT = (
    ROOT / "data" / "servers"
)

print(SOFTWARE_DATA_FILE)