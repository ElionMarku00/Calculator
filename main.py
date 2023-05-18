import dearpygui.dearpygui as dpg
from callbacks import *
from windows import setup_UI
from History import History


#TODO: adjust history window to be visible 
#
if __name__ == '__main__':

    setup_UI()

    # add a font registry
    # with dpg.font_registry():
    # first argument ids the path to the .ttf or .otf file
    # default_font = dpg.add_font("times.ttf", 20)

    # def on_selection(sender, data):
    #     selected_item = hist[data[0]]
    #     print(f"Selected item: {selected_item}")


    # dpg.bind_font(default_font)
