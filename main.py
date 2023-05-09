from button import Button
import dearpygui.dearpygui as dpg
from callbacks import *

from History import History

dpg.create_context()

temp = []
numbers = []
hist = History()
# The list of main buttons to use plus the callback function if it is not the default one
button_list = [[['('], [')'], ['c',clear_callback], ['<--',backspace_callback]], [[7], [8], [9], ['%']], [[4], [5], [6], ["*"]], [[1], [2], [3], ["-"]], [["+/-"], [0], ['.'], ['+']]]

# add a font registry
# with dpg.font_registry():
# first argument ids the path to the .ttf or .otf file
# default_font = dpg.add_font("times.ttf", 20)

def on_selection(sender, data):
    selected_item = hist[data[0]]
    print(f"Selected item: {selected_item}")

def toggleHistory(sender, app_data, user_data):
    
    x, y = dpg.get_item_pos(primaryWindow)
    width, height = dpg.get_item_rect_size(primaryWindow)
    
    dpg.set_item_pos(histwindow, [ x+width, y])
    if not dpg.is_item_shown('historyWindow'):
        dpg.show_item('historyWindow')
    else: dpg.hide_item('historyWindow')

dpg.create_context()

# dpg.bind_font(default_font)
with dpg.window(label="Tutorial", tag="Primary Window") as primaryWindow:
    dpg.add_separator()
    Button('history', toggleHistory)
    dpg.add_text("", tag="Display")
    dpg.add_separator()

    dpg.add_separator()
    with dpg.group(horizontal=True):
        Button("sin", num_callback, button_type='trigo')
        Button("cos", num_callback, button_type='trigo')
        Button("tan", num_callback, button_type='trigo')
        # TODO based on the button_type chnage the default value. for trigono we need to put the 0
    dpg.add_separator()
    with dpg.table(tag="Table", header_row=False):
        # add columns to the table
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()
        dpg.add_table_column()
        
        for row in button_list:
            # create a row and read one of the nested list items
            with dpg.table_row():
                # if there is a callback specified which is not the default one, use that. otherwise use the defualt one in the ___init___
                [Button(sublist[0]) if len(sublist) == 1 else Button(sublist[0], callback_function=sublist[1]) for sublist in row]

    # Button('=', result_callback, user_data=hist)
    #TODO add user data to the button class
    dpg.add_button(label="=", width=165, height=50, callback=result_callback, user_data=hist)

with dpg.window(label="history", tag="historyWindow",show=False) as histwindow:
#    if len(hist._data) > 0:
    dpg.add_listbox(label="Operations",items=[str(x) for x in hist._data ], tag="List")
with dpg.handler_registry():
    dpg.add_key_press_handler(callback=type_text)

dpg.create_viewport(title='Custom Title', width=200, height=800)
dpg.setup_dearpygui()
dpg.show_viewport()
# dpg.set_primary_window("Primary Window", True)
dpg.start_dearpygui()
dpg.destroy_context()

# make a class for buttons
# make the functions
# make the gui
# profit
