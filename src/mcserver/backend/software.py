from functools import cache

import yaml

from mcserver.settings import SOFTWARE_DATA_FILE


@cache
def get_software_data():
    with open(SOFTWARE_DATA_FILE, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return data["softwares"]


def get_software_names():
    return list(get_software_data().keys())
