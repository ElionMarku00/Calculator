# This class holds the implementations of windows we see, like main and history
from button import Button
import dearpygui.dearpygui as dpg
from callbacks import *

from History import History
from abc import ABC, abstractmethod

# The list of main buttons to use plus the callback function if it is not the default one
button_list = [[["tan", trigo_callback], ["sin", trigo_callback], ["cos", trigo_callback], ["cot", trigo_callback]],
               [['('], [')'], ['c', clear_callback], ['<--', backspace_callback]], [[7], [8], [9], ['%']],
               [[4], [5], [6], ["*"]], [[1], [2], [3], ["-"]], [["+/-"], [0], ['.'], ['+']]]


class BaseWindowClass(ABC):

    def __init__(self, name):
        self.name = name

    # this abstract method contains the buttons and items we see in the window
    @abstractmethod
    def init_window(self):
        pass


class MainWindow(BaseWindowClass):
    def init_window(self):
        with dpg.window(label="Tutorial", tag="Primary Window") as primaryWindow:
            dpg.add_separator()
            Button('history', callback_function=toggleHistory, user_data=primaryWindow, width=90)
            dpg.add_separator()
            dpg.add_text("0", tag="Display")

            dpg.add_separator()

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
                        # if there is a callback specified which is not the default one, use that. otherwise use the
                        # default one in the ___init___
                        [Button(sublist[0]) if len(sublist) == 1 else Button(sublist[0], callback_function=sublist[1])
                         for
                         sublist in row]

            # Button('=', result_callback, user_data=hist)
            # TODO add user data to the button class
            # dpg.add_button(label="=", width=165, height=50, callback=result_callback, user_data=hist)
            dpg.add_button(label="=", width=165, height=50, callback=result_callback)

    def __init__(self, name):
        super().__init__(name)
        self.init_window()


# TODO finish implementaion
class HistoryWindow(BaseWindowClass):

    def __init__(self, name):
        super().__init__(name)
        self.init_window()

    def init_window(self,):
        print(self.name,'is the name of historywindow')

        hist = History()

        with dpg.window(label="history", tag=self.name, show=False) as histwindow:
        #    if len(hist._data) > 0:
            dpg.add_listbox(label="Operations", items=[str(x) for x in hist._data ], tag="List")
        pass
