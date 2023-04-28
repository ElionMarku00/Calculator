import dearpygui.dearpygui as dpg


def result_callback(sender, data):
    current_value = dpg.get_value("Display")
    dpg.set_value("Display", str(eval(current_value)))
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


def add_callback(sender, data):
    current_value = dpg.get_value("Display")
    dpg.set_value("Display", str(current_value) + str("+"))


def sub_callback(sender, data):
    current_value = dpg.get_value("Display")
    dpg.set_value("Display", str(current_value) + str("-"))


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