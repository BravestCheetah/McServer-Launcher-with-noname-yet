import yaml
from nicegui import ui

from mcserver.settings import SOFTWARE_DATA_FILE


def _get_software_list():
    with open(SOFTWARE_DATA_FILE, "r") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
    return list(data["softwares"].keys())


def content():
    ui.label("DEBUG")

    ui.label("software")
    ui.select(
        options=_get_software_list(),
        with_input=True,
        on_change=lambda e: ui.notify(e.value),
    ).classes("w-40")
