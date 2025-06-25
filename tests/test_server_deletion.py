import hashlib
import pathlib


def test_server_creation():
    from mcserver.backend.server_manager import delete_server, create_server


    software = "paper"
    version = "1.18"

    server = create_server("deletionTest", "hi", software, version)
    
    delete_server("deletionTest")

    assert pathlib.Path.exists(server.path)