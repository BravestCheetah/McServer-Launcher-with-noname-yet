import hashlib


def test_vanilla_jar_download():
    from mcserver.backend.server import Server

    software = "vanilla"
    version = "1.21.6"
    sha1 = "6e64dcabba3c01a7271b4fa6bd898483b794c59b"
    server = Server("test", software=software, version=version)
    server.download_jar()

    with open(server.jar_file, "rb") as f:
        assert hashlib.sha1(f.read()).hexdigest() == sha1
