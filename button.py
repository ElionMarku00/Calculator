import dearpygui.dearpygui as dpg


class Button:
    def __init__(self, value, callback_function):
        dpg.add_button(label=str(value), width=50, height=50, callback=callback_function)
