# McServer Launcher
A Launcher And Manager For Vanilla and modified Minecraft Server

## Running

First, make sure you have [uv](https://docs.astral.sh/uv) installed, then simply
execute it with:

```bash
uv run main.py
```

The embedded server should start the application on http://localhost:8080.


**Note**: If you use the numeric IP address (like 127.0.0.1) instead of `localhost` some
CSS might fail to load depending on your browser, so make sure you're using `localhost`.

## Developing

The embedded server has live-reload enabled, so any changes made to `main.py`
should be automatically reflected in the open webpage. To develop locally you need
to make sure the package is installed on edit mode:

```bash
uv sync
```

### Testing

Tests are implemented using [pytest](https://docs.pytest.org/en/stable/) and
can be executed with:

```bash
uv run pytest
```

**NOTE**: some tests will download content from the Internet into your machine,
make sure you have the disk space and permissions to write them or they will fail
