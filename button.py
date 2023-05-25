import dearpygui.dearpygui as dpg

from callbacks import num_callback
# This file contains the button class

class Button:
    def __init__(self, value, user_data=None, callback_function=num_callback, width=100, height=50,
                 button_type='default'):
        dpg.add_button(
            label=str(value),
            width=width,
            height=height,
            callback=callback_function,  # the default callback funtion
            # user_data=button_type,
            user_data=user_data,
            tag=value)
