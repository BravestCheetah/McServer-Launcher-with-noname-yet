import requests as req
import yaml
try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper
import pathlib
from ..root_path import get_root_path
from ..misc.errors import *



class _server_downloads():
    def __init__(self):

        try:
            with open(pathlib.Path.joinpath(get_root_path(), "data", "meta", "downloads.yaml"), "r") as f:
                self.download_data = yaml.load(f, Loader=yaml.FullLoader)
        except Exception as e:
            raise LoadDownloadsDataError(f"An Error Occured When Loading downloads.yaml: {e}")



    def get_json(self, url: str) -> dict:
        resp = req.get(url)

        if resp.ok: return resp.json()
        else: raise RequestJsonFailedError(f"An Error Occured When Getting JSON From Url {url}"); return {}



    def vanilla(self, ver: str) -> pathlib.Path:
        """
        Proccess:
        get version manifest from the minecraft servers
        get the manifest url for the version we want from the version manifest
        get the server download from the versions own manifest
        return the download link
        """

        manifest_url = self.download_data["softwares"]["vanilla"]["version-manifest"]
        ver_manifest = self.get_json(manifest_url)

        versions = ver_manifest["versions"]
        for version in versions:
            if version["id"] == ver:
                ver_data = version
                break

        ver_manifest_url = ver_data["url"]
        ver_manifest = self.get_json(ver_manifest_url)

        jar_download = ver_manifest["downloads"]["server"]["url"]

        return jar_download



class data():
    def __init__(self) -> None:
        self.downloads = _server_downloads()

        self._software_commands = {
            "vanilla": self.downloads.vanilla
        }

    def get_jar_download(self, software, ver) -> None:
        command = self._software_commands[software]
        return command(ver)


d = data()
print(d.get_jar_download("1.13"))