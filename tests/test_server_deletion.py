import hashlib
import pathlib


def test_server_creation():
    from mcserver.backend.server_manager import delete_server, create_server
    from mcserver.backend.data import get_servers, rm_server

    if "deletiontest" in get_servers():
        rm_server("deletiontest", confirm=True)

    software = "paper"
    version = "1.18"

    server = create_server("deletiontest", "hi", software, version)
    
    delete_server("deletiontest")

    assert pathlib.Path.exists(server.path)