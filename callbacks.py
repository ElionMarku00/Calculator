import dearpygui.dearpygui as dpg
import math
from math import sin, cos, tan


def result_callback(sender, data, user_data):
    
    print(sender,data,user_data, 'from result_callback')
    current_value = dpg.get_value("Display")
    res = str(eval(current_value))
    dpg.set_value("Display", res)

    # store operation and result in history
    hist = user_data
    hist.saveToHistory(current_value, res)
    print(hist._data[0])

    # refresh list
    dpg.configure_item("List", items=[str(x) for x in hist._data])

    # add the last number that is inside the temp list, since we do not run the add callback for it
    # last_num = int(''.join(str(item) for item in temp))
    # numbers.append(last_num)
    # temp.clear()
    # ###
    # # calculate the sum of all numbers in the "numbers" list
    # result = sum([num for num in numbers])
    # # print the numbers list to the console for debugging purposes
    # print(numbers)
    # # set the value of the "Display" item to the calculated result
    # dpg.set_value("Display", str(result))
    # # clear the "numbers" list for the next calculation
    # numbers.clear()


def toggleHistory(sender, app_data, user_data):

    print(sender, app_data, user_data)

    x, y = dpg.get_item_pos(user_data)
    
    width, height = dpg.get_item_rect_size(user_data)

    
    dpg.set_item_pos('historyWindow', [x + width, y])
    if not dpg.is_item_shown('historyWindow'):
        dpg.show_item('historyWindow')
    else:
        dpg.hide_item('historyWindow')
    


def trigo_callback(sender, data):
    trigonometry_function = dpg.get_item_label(sender)
    current_display_value = dpg.get_value("Display")
    dpg.set_value("Display", str(trigonometry_function) + '(' + str(current_display_value) + ')')


def num_callback(sender, data):
    digit = dpg.get_item_label(sender)
    current_value = dpg.get_value("Display")
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
