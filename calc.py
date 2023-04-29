import dearpygui.dearpygui as dpg

# create a context for the GUI
dpg.create_context()

# initialize two empty lists to store temporary and final values
temp = []
numbers = []

def result_callback(sender, data):
    # add the last number that is inside the temp list, since we do not run the add callback for it
    last_num = int(''.join(str(item) for item in temp))
    numbers.append(last_num)
    temp.clear()
    ###
    # calculate the sum of all numbers in the "numbers" list
    result = sum([num for num in numbers])
    # print the numbers list to the console for debugging purposes
    print(numbers)
    # set the value of the "Display" item to the calculated result
    dpg.set_value("Display", str(result))
    # clear the "numbers" list for the next calculation
    numbers.clear()


def num_callback(sender, data):
    # get the digit of the button that was pressed and add it to the "temp" list
    digit = dpg.get_item_label(sender)
    temp.append(digit)
    # get the current value of the "Display" item
    current_value = dpg.get_value("Display")
    # update the "Display" item to show the new value
    dpg.set_value("Display", str(current_value) + str(int(digit)))

# create a window with a table to hold the buttons
with dpg.window(label="Tutorial"):
    dpg.add_separator()
    dpg.add_text("", tag="Display")
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
                        dpg.add_button(label="+", width=50, height=50, callback=add_callback)
                    elif i * 3 + j + 1 == 12:
                        # add a button for subtraction
                        dpg.add_button(label="-", width=50, height=50)
                    elif i * 3 + j + 1 == 11:
                        # add a button for 0
                        dpg.add_button(label="0", width=50, height=50, callback=num_callback)
                    else:
                        # add a button for the number
                        dpg.add_button(label=str(i * 3 + j + 1), width=50, height=50, callback=num_callback)
        # add a row for the equals button
        with dpg.table_row():
            dpg.add_button(label="=", width=50, height=50, callback=result_callback)





dpg.create_viewport(title='Custom Title', width=800, height=600)
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

# make a class for buttons
# make the functions 
# make the gui 
#profit


# Your application won't reach here until you exit and the event
# loop has stopped.
