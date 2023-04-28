import dearpygui.dearpygui as dpg
from button import Button

from callbacks import result_callback, add_callback, sub_callback, num_callback, clear_callback, backspace_callback,type_text

dpg.create_context()

temp = []
numbers = []

# add a font registry
# with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    # default_font = dpg.add_font("times.ttf", 20)



# dpg.bind_font(default_font)
with dpg.window(label="Tutorial", tag="Primary Window"):
    dpg.add_separator()
    dpg.add_text("", tag="Display")
    dpg.add_separator()
    Button('<--', backspace_callback)
    dpg.add_separator()
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
                    if i * 3 + j + 1 == 10:
                        Button("+", add_callback)
                    elif i * 3 + j + 1 == 12:
                        Button("-", sub_callback)
                    elif i * 3 + j + 1 == 11:
                        Button("0", num_callback)
                    else:
                        Button(str(i * 3 + j + 1), num_callback)
        with dpg.table_row():
            Button('(', num_callback)
            Button(')', num_callback)
            Button('C', clear_callback)
    dpg.add_button(label="=", width=165, height=50, callback=result_callback)


with dpg.handler_registry():
    dpg.add_key_press_handler( callback=type_text)


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
