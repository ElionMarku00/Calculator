import dearpygui.dearpygui as dpg
import math
from math import sin, cos, tan, factorial, log10, log2
import re
from functools import reduce

# This file contains all the callback method used when clicking a button
# checks if the last button that was clicked was the result button
result_calculated = False

# calculates the value showed on the display when the "=" button is clicked
def result_callback(sender, data, user_data):
    # defines new functions that are not supported by default
    local_vars = {"abslt": lambda x: x if x >= 0 else -x, "pot": lambda x: x ** 2, "sqrt": lambda x: x ** 0.5,
                  "!": lambda x: factorial(x)
             
                  }
    global_vars = {}
    current_value = dpg.get_value("Display")
    try:
        res = str(eval(current_value, global_vars, local_vars))
        dpg.set_value("Display", res)
    except ZeroDivisionError:  # catching divided by zero
        dpg.set_value("Display", 'Cannot divide by zero')
    except SyntaxError:
         dpg.set_value("Display", 'Format Error, press c to clear')
    # change the boolean
    global result_calculated
    result_calculated = True
    # store operation and result in history
    hist = user_data
    hist.saveToHistory(current_value, res)

    # refresh list
    dpg.configure_item("List", items=[str(x) for x in hist._data])

# def toggleHistory(sender, app_data, user_data):
#     # place history window next to main window
#     x, y = dpg.get_item_pos(user_data)
#     width, height = dpg.get_item_rect_size(user_data)
#     dpg.set_item_pos('historyWindow', [x + width, y])

#     # add or hide historyWindow on buttonClick
#     if not dpg.is_item_shown('historyWindow'):
#         dpg.show_item('historyWindow')
#         window_size = dpg.get_item_rect_size("Primary Window")
#         dpg.set_viewport_size(width=window_size[0], height=window_size[1])
#     else:
#         dpg.hide_item('historyWindow')

# used in trigonometry, square root and power of two

'''
old
'''
# def advance_op_callback(sender, data):
#     global result_calculated
#     result_calculated = False
#     trigonometry_function = dpg.get_item_label(sender)
#     current_display_value = dpg.get_value("Display")
    
#     dpg.set_value("Display", str(trigonometry_function) + '(' + str(current_display_value) + ')')

'''
new, now we can type stuff like cos(0) + sin(0)
'''
def advance_op_callback(sender, data):
    global result_calculated
    result_calculated = False
    trigonometry_function = dpg.get_item_label(sender)
    current_display_value = dpg.get_value("Display")
    
    pattern = r"([-+*/])"
    where_to_add_trig = re.split(pattern, current_display_value )

    oldInput = reduce( lambda x, y: x + y ,where_to_add_trig[:len(where_to_add_trig) - 1],"")
    print('oldInput',oldInput)
    dpg.set_value("Display", oldInput + str(trigonometry_function) + '(' + str(where_to_add_trig[-1]) + ')')

def num_callback(sender, data):
    current_value = dpg.get_value("Display")
    global result_calculated
    # if the result button was clicked or the first number on the screen is zero, clear the screen
    if result_calculated or current_value[0] == '0':
        dpg.set_value("Display", '')
        # now that the result button is not the last button clicked, change the bool
        result_calculated = False
    digit = dpg.get_item_label(sender)
    current_value = dpg.get_value("Display")
    dpg.set_value("Display", str(current_value) + str(digit))

# used for basic mathematical operations
def operator_callback(sender, data):
    global result_calculated
    result_calculated = False

    digit = dpg.get_item_label(sender)
    current_value = dpg.get_value("Display")
    # if the last item on display is an operator, replace it with the new one. used to prevent adding extra operator
    if current_value[-1] in ['+', '-', '*', '/']:
        dpg.set_value("Display", str(current_value[:-1]) + str(digit))
    else:
        dpg.set_value("Display", str(current_value) + str(digit))


# reset the diplay to default value
def clear_callback():
    dpg.set_value("Display", '0')



# removes one character from the display
def backspace_callback():
    current_value = dpg.get_value("Display")

    if len(current_value) == 1:
        dpg.set_value("Display", '0')
    else:
        dpg.set_value("Display", str(current_value)[:-1])


def type_text(sender, app_data):
    print('type_text',sender,app_data)
    if str(chr(app_data)).isnumeric():
        dpg.set_value("Display", f'{dpg.get_value("Display")}{chr(app_data)}')
