import hashlib


def test_server_creation():
    from mcserver.backend.server import Server
    from mcserver.backend.data import load_server_data, rm_server


    software = "vanilla"
    version = "1.21.6"

    rm_server("test", confirm=True)

    server = Server(name="test", motd="testing server", software=software, version=version)
    server.install_server()

    desired_data = {
        "name": "test",
        "motd": "testing server",
        "version": version,
        "software": software,
    }

    data = load_server_data()["test"]

    assert data == desired_data