# This File holds the implementations of windows we see, like main and history
from button import Button
import dearpygui.dearpygui as dpg
from callbacks import *

from History import History
from abc import ABC, abstractmethod

# The list of main buttons to use plus the callback function if it is not the default one
button_list = [[["tan", advance_op_callback], ["sin", advance_op_callback], ["cos", advance_op_callback], ["cot", advance_op_callback]],
               [['('], [')'], ['c', clear_callback], ['<--', backspace_callback]],
               [['sqrt', advance_op_callback], ['pot', advance_op_callback], ['abslt', advance_op_callback],['%',operator_callback]],
               [[7], [8], [9], ['/']],
               [[4], [5], [6], ["*", operator_callback]], [[1], [2], [3], ["-", operator_callback]],
               [["+/-", operator_callback], [0], ['.', operator_callback], ['+', operator_callback]]]


class BaseWindowClass(ABC):

    def __init__(self, name, history=None):
        self.name = name
        self.history = history

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

            Button('=', callback_function=result_callback, width=165, height=50, user_data=self.history)


    def __init__(self, name, history):
        super().__init__(name, history)
        self.init_window()


class HistoryWindow(BaseWindowClass):

    def __init__(self, name, history=None):
        super().__init__(name, history)
        self.init_window()

    def init_window(self, ):
        print(self.name, 'is the name of historywindow')

        with dpg.window(label="history", tag=self.name, show=False) as histwindow:
            #    if len(hist._data) > 0:
            dpg.add_listbox(label="Operations", items=[str(x) for x in self.history._data], tag="List")
