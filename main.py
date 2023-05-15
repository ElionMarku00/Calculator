import dearpygui.dearpygui as dpg
from callbacks import *
from windows import *
from History import History

if __name__ == '__main__':


    dpg.create_context()

    # hist is initialized on main.py so both mainwindow and historywindow get the same object. 
    hist = History()

    # add a font registry
    # with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    # default_font = dpg.add_font("times.ttf", 20)

    main_window = MainWindow('Tutorial', hist)
    history_window = HistoryWindow('historyWindow', hist)

    # def on_selection(sender, data):
    #     selected_item = hist[data[0]]
    #     print(f"Selected item: {selected_item}")


    dpg.create_context()

    # dpg.bind_font(default_font)

    # with dpg.window(label="history", tag="historyWindow", show=False) as histwindow:
    #     #    if len(hist._data) > 0:
    #     dpg.add_listbox(label="Operations", items=[str(x) for x in hist._data], tag="List")
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
