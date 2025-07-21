import argparse
from nicegui import ui

from mcserver.webui import index

if __name__ in {"__main__", "__mp_main__"}:
    index.render()
