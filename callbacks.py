import dearpygui.dearpygui as dpg
import math
from math import sin, cos, tan

# checks if the last button that was clicked was the result button
result_calculated = False


def result_callback(sender, data, user_data):
    current_value = dpg.get_value("Display")
    try:
        res = str(eval(current_value))
        dpg.set_value("Display", res)
    except ZeroDivisionError:  # catching divided by zero
        dpg.set_value("Display", 'Cannot divide by zero')
    global result_calculated
    result_calculated = True
    # store operation and result in history
    hist = user_data
    hist.saveToHistory(current_value, res)

    # refresh list
    dpg.configure_item("List", items=[str(x) for x in hist._data])


def toggleHistory(sender, app_data, user_data):
    # place history window next to main window
    x, y = dpg.get_item_pos(user_data)
    width, height = dpg.get_item_rect_size(user_data)
    dpg.set_item_pos('historyWindow', [x + width, y])

    # add or hide historyWindow on buttonClick
    if not dpg.is_item_shown('historyWindow'):
        dpg.show_item('historyWindow')
    else:
        dpg.hide_item('historyWindow')


def trigo_callback(sender, data):
    trigonometry_function = dpg.get_item_label(sender)
    current_display_value = dpg.get_value("Display")
    dpg.set_value("Display", str(trigonometry_function) + '(' + str(current_display_value) + ')')


def num_callback(sender, data):
    current_value = dpg.get_value("Display")
    global result_calculated
    # if the result button was clicked or the first number on the screen is zero, clear the screen
    if result_calculated or current_value[0] == '0':
        dpg.set_value("Display", '')
        result_calculated = False
    digit = dpg.get_item_label(sender)
    current_value = dpg.get_value("Display")
    dpg.set_value("Display", str(current_value) + str(digit))


def operator_callback(sender, data):
    digit = dpg.get_item_label(sender)
    current_value = dpg.get_value("Display")
    # if the last item on display is an operator, replace it with the new one
    if current_value[-1] in ['+', '-', '*', '/']:
        dpg.set_value("Display", str(current_value[:-1]) + str(digit))
    else:
        dpg.set_value("Display", str(current_value) + str(digit))


def clear_callback():
    dpg.set_value("Display", '')


def backspace_callback():
    current_value = dpg.get_value("Display")
    dpg.set_value("Display", str(current_value)[:-1])


def type_text(sender, app_data):
    print(app_data)
    if str(chr(app_data)).isnumeric():
        dpg.set_value("Display", f'{dpg.get_value("Display")}{chr(app_data)}')
