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

    server = Server(software, version, "test", "motd")
    server.install_server()

    desired_data = {
        "disp_name": "test",
        "motd": "motd",
        "version": version,
        "software": software,
    }

    data = load_server_data()["test"]

    assert data == desired_data