from nicegui import ui


def render():
    with ui.row():
        ui.button("Server A")
        ui.button("Server B")
        ui.button("Server C")
