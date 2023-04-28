import dearpygui.dearpygui as dpg
from button import Button

# create a context for the GUI
dpg.create_context()

# initialize two empty lists to store temporary and final values
temp = []
numbers = []

# add a font registry
with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    default_font = dpg.add_font("times.ttf", 20)


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
    # get the current value of the "Display" item
    current_value = dpg.get_value("Display")
    # update the "Display" item to show the current value with a plus sign
    dpg.set_value("Display", str(current_value) + str("+"))


def sub_callback(sender, data):
    # get the current value of the "Display" item
    current_value = dpg.get_value("Display")
    # update the "Display" item to show the current value with a plus sign
    dpg.set_value("Display", str(current_value) + str("-"))


def num_callback(sender, data):

    # get the digit of the button that was pressed
    digit = dpg.get_item_label(sender)
    # temp.append(digit)
    # get the current value of the "Display" item
    current_value = dpg.get_value("Display")
    # update the "Display" item to show the new value
    dpg.set_value("Display", str(current_value) + str(digit))


def clear_callback():
    dpg.set_value("Display", '')
def backspace_callback():
    # get the current value of the "Display" item
    current_value = dpg.get_value("Display")
    dpg.set_value("Display", str(current_value)[:-1])

# create a window with a table to hold the buttons
dpg.bind_font(default_font)
with dpg.window(label="Tutorial", tag="Primary Window"):
    dpg.add_separator()
    dpg.add_text("", tag="Display")
    dpg.add_separator()
    Button('<--', backspace_callback)
    dpg.add_separator()
    # adding trigonometry
    with dpg.group(horizontal=True):
        Button("sin", num_callback, button_type='trigo')
        Button("cos", num_callback, button_type='trigo')
        Button("tan", num_callback, button_type='trigo')
        #TODO based on the button_type chnage the default value. for trigono we need to put the 0
    dpg.add_separator()
    with dpg.table(tag="Table", header_row=False):
        # add three columns to the table
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()
        for i in range(0, 4):
            with dpg.table_row():
                for j in range(0, 3):
                    # add a button for each number, except 0 and 10
                    if i * 3 + j + 1 == 10:
                        # add a button for addition
                        Button("+", add_callback)
                    elif i * 3 + j + 1 == 12:
                        # add a button for subtraction
                        Button("-", sub_callback)
                    elif i * 3 + j + 1 == 11:
                        # add a button for 0
                        Button("0", num_callback)
                    else:
                        # add a button for the number
                        Button(str(i * 3 + j + 1), num_callback)
        with dpg.table_row():
            Button('(', num_callback)
            Button(')', num_callback)
            Button('C', clear_callback)
    dpg.add_button(label="=", width=165, height=50, callback=result_callback)

dpg.create_viewport(title='Custom Title', width=200, height=500)
dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

# make a class for buttons
# make the functions
# make the gui
# profit
