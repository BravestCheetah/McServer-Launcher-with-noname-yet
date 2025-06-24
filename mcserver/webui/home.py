from nicegui import ui


def render() -> None:
    ui.label("This is the home page.").classes("font-bold")
    ui.label("Use the menu on the top right to navigate.")
