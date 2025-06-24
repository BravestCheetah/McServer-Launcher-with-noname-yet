from contextlib import contextmanager

from nicegui import ui


@contextmanager
def frame():
    with ui.header():
        with ui.tabs():
            ui.tab("A")
            ui.tab("B")
            ui.tab("C")
    yield
