import pathlib
import requests

from mcserver.backend.data import get_software_metadata
from mcserver.errors import UnknownSoftwareError, UnknownVersionError, RequestJsonFailedError


class ServerDownloader:
    def get_url(self, version: str) -> str:
        raise NotImplementedError
    

    def get_json(self, url: str) -> dict:
        resp = requests.get(url)

        if resp.ok:
            return resp.json()
        else:
            raise RequestJsonFailedError(
                f"An Error Occured When Getting JSON From Url {url}"
            )
            return {}

    def download(self, version: str, path: pathlib.Path) -> pathlib.Path:
        path.parent.mkdir(parents=True, exist_ok=True)
        url = self.get_url(version)

        with requests.get(url, stream=True) as r:
            with open(path, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

        return path


class VanillaDownloader(ServerDownloader):
    def get_release_data(self, manifest: dict, version: str) -> dict:
        for v in manifest["versions"]:
            if v["id"] == version:
                return v
        else:
            raise UnknownVersionError(version)

    def get_url(self, version: str) -> str:
        """
        Proccess:
        get version manifest from the minecraft servers
        get the manifest url for the version we want from the version manifest
        get the server download from the versions own manifest
        return the download link
        """

        manifest_url = get_software_metadata("vanilla")["version-manifest"]
        manifest = requests.get(manifest_url).json()

        release_data = self.get_release_data(manifest, version)

        release_manifest_url = release_data["url"]
        release_manifest = requests.get(release_manifest_url).json()

        return release_manifest["downloads"]["server"]["url"]

class PaperDownloader(ServerDownloader):
    def get_release_data(self, manifest: dict, version: str) -> dict:
        data_url = get_software_metadata["versions-data"]

        ver_data_url = f"{data_url}{version}"
        ver_data = self.get_json(ver_data_url)

        latest_build = ver_data["builds"][-1]
        build_info_url = f"{data_url}{version}/builds/{latest_build}"

        build_info = self.get_json(build_info_url)
        return build_info


    def get_url(self, version: str) -> str:
        data_url = self.download_data["softwares"]["paper"]["versions-data"]

        build_info = self.get_release_data()
        latest_build = build_info["builds"][-1]

        build_name = build_info["downloads"]["application"]["name"]
        build_download = f"{data_url}{version}/builds/{latest_build}/downloads/{build_name}"

        return build_download


DOWNLOADERS = {
    "vanilla": VanillaDownloader,
    "paper": PaperDownloader,
}


def get_downloader(software: str) -> ServerDownloader:
    try:
        return DOWNLOADERS[software]()
    except KeyError:
        raise UnknownSoftwareError(software)
