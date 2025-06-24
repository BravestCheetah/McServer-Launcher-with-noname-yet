from nicegui import ui

from mcserver.backend.data import get_software_names


def render():
    ui.label("DEBUG")

    ui.label("software")
    ui.select(
        options=get_software_names(),
        with_input=True,
        on_change=lambda e: ui.notify(e.value),
    ).classes("w-40")
