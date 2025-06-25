import hashlib


def test_server_creation():
    from mcserver.backend.server import Server
    from mcserver.backend.data import load_server_data, rm_server


    software = "paper"
    version = "1.18"

    try:
        rm_server("test", confirm=True)
    except Exception:
        pass

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