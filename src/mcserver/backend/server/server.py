import platform
import signal
import subprocess

from slugify import slugify

from mcserver.backend.server.downloader import get_downloader
from mcserver.settings import SERVER_ROOT


class Server:
    def __init__(
        self,
        software: str,
        version: str,
        name: str,
        motd: str = "",
    ) -> None:
        self.name = name
        self.motd = motd
        self.software = software
        self.version = version

        # self.server_data = data()

    @property
    def path(self):
        return SERVER_ROOT / slugify(self.name)

    @property
    def jar_file(self):
        return self.path / "server.jar"

    def download_jar(self):
        downloader = get_downloader(self.software)
        downloader.download(self.version, self.jar_file)

    def install_server(self):
        self.download_jar()

        eula_path = self.path / "eula.txt"

        with open(eula_path, "w") as f:
            f.write("eula=true")

    def start_server(self):
        self.process = subprocess.Popen(["java", "-jar", "server.jar"], cwd=self.path)

    def kill_server(self):
        if platform.system() == "Windows":
            self.process.send_signal(signal.CTRL_BREAK_EVENT)
        else:
            self.process.send_signal(signal.SIGINT)

        self.process.wait()

    def restart_server(self):
        self.kill_server()
        self.start_server()
