from nicegui import ui

from mcserver.webui import home, theme


@ui.page("/")
def index():
    with theme.frame():
        home.render()


ui.run(title="MC Server")
