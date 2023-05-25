import dearpygui.dearpygui as dpg
from callbacks import *
from windows import setup_UI
from History import History


#TODO fix % and +/- and cot  button
# add cot
# i deactivated keypress handler because when we input in history searchbar, the input is added to Display also. 

#if i were to start with 0 / number, we get invalid syntax 
#when pressing 0 + a number at the start 
#optionally make an enum with window labels so we don't have to remember them each time
#optionally add radian or degrees for the trig functions.
#optional add factorial
# we could combine '(' and  ')' into one button and add one more function 
if __name__ == '__main__':

    setup_UI()
