from nicegui import ui
from backend.root_path import get_root_path

ui.label("Current App Path: " + str(get_root_path()))
ui.run()