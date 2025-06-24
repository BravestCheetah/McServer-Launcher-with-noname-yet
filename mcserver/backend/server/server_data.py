import requests as req
from misc.errors import RequestJsonFailedError



class _server_downloads():
    def __init__(self):
        pass

    def get_json(self, url):
        resp = req.get(url)

        if resp.ok: return resp.json()
        else: raise RequestJsonFailedError(f"An Error Occured When Getting JSON From Url {url}")

    def vanilla(self):
        pass



class data():
    def __init__(self) -> None:
        self.downloads = _server_downloads()

    def get_jar_download(software, ver) -> None:
        pass

