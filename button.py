import dearpygui.dearpygui as dpg




class Button:
    def __init__(self, value, callback_function, width=50, height=50, button_type='default'):
        dpg.add_button(label=str(value), width=width, height=height, callback=callback_function, user_data=button_type,tag=value)