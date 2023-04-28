import dearpygui.dearpygui as dpg


class Windows:
    name = ''

    def __init__(self, name, create_page):
        self.name = name
        create_page()
