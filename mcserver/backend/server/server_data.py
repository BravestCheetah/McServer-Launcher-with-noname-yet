import requests as req
import yaml
from misc.errors import RequestJsonFailedError
import pathlib
from root_path import get_root_path
import misc.errors as err



class _server_downloads():
    def __init__(self):
        
        try:
            with open(pathlib.Path.joinpath(get_root_path(), "data", "meta", "downloads.yaml"), "r") as f:
                self.download_data = yaml.load(f)
        except Exception as e:
            raise err.LoadDownloadsDataError(f"An Error Occured When Loading downloads.yaml: {e}")

    def get_json(self, url):
        resp = req.get(url)

        if resp.ok: return resp.json()
        else: raise RequestJsonFailedError(f"An Error Occured When Getting JSON From Url {url}"); return

    def vanilla(self):

        self.get_json()



class data():
    def __init__(self) -> None:
        self.downloads = _server_downloads()

    def get_jar_download(software, ver) -> None:
        pass

