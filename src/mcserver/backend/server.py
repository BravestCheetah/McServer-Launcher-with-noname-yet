import platform
import signal
import subprocess
import pathlib
import shutil

from slugify import slugify

from mcserver.backend.downloader import get_downloader
from mcserver.settings import SERVER_ROOT
from mcserver.backend.data import add_server, edit_server


class Server:
    def __init__(
        self,
        software: str,
        version: str,
        disp_name: str,
        motd: str = "",
    ) -> None:

        self.motd = motd
        self.software = software
        self.version = version

        self.disp_name = disp_name
        self.name = slugify(self.disp_name)

        # self.server_data = data()

    @property
    def path(self):
        return SERVER_ROOT / self.name

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
        
        properties_path = self.path / "server.properties"

        with open(properties_path, "w") as f:
            f.write(f"motd={self.motd}")
        
        add_server(self.name, self.motd, self.version, self.software)

    def uninstall_server(self):
        shutil.rmtree(self.path)

    def start_server(self):
        self.process = subprocess.run(["java", "-jar", "server.jar"], cwd=self.path)

    def kill_server(self):
        if platform.system() == "Windows":
            self.process.send_signal(signal.CTRL_BREAK_EVENT)
        else:
            self.process.send_signal(signal.SIGINT)

        self.process.wait()

    def restart_server(self):
        self.kill_server()
        self.start_server()
