console_log_container = None


def add_log_message(text: str):
    

    if console_log_container:

        with console_log_container:

            from nicegui import ui
            ui.label(text)


        console_log_container.parent.scroll_to(console_log_container)

    else:
        
        print("[Console Not Ready] " + text)
