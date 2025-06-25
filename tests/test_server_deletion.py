import hashlib
import pathlib


def test_server_creation():
    from mcserver.backend.server import Server
    from mcserver.backend.data import rm_server


    software = "paper"
    version = "1.18"

    server = Server(name="test2", motd="testing server", software=software, version=version)
    server.install_server()

    rm_server("test2", confirm=True)

    assert pathlib.Path.exists(server.path)