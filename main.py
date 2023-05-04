from button import Button
import dearpygui.dearpygui as dpg

from callbacks import num_callback, type_text, result_callback

# The list of main buttons to use
button_list = [['(', ')', 'c', '<--'], [7, 8, 9, '%'], [4, 5, 6, "*"], [1, 2, 3, "-"], ["+/-", 0, '.', '+']]

# add a font registry
# with dpg.font_registry():
# first argument ids the path to the .ttf or .otf file
# default_font = dpg.add_font("times.ttf", 20)

dpg.create_context()

# dpg.bind_font(default_font)
with dpg.window(label="Tutorial", tag="Primary Window"):
    dpg.add_separator()
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
        for i in range(0, len(button_list)):
            # create a row and read one of the nested list items
            with dpg.table_row():
                [Button(x, num_callback) for x in button_list[i]]
    Button('=', result_callback)
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
