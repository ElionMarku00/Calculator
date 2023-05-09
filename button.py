import dearpygui.dearpygui as dpg

from callbacks import num_callback

class Button:
    def __init__(self, value, callback_function=num_callback, width=50, height=50, button_type='default'):
        dpg.add_button(
            label=str(value), 
                        width=width,
                        height=height,
                        callback=callback_function, #the default callback funtion
                        user_data=button_type,
                        tag=value)
