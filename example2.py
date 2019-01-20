import curses
import random
from time import sleep
import threading


def ksp():
    yield {random.randint(1000, 9999)}



def tui(stdscr):
    # setup
    curses.curs_set(False) # cursor visibility
    curses.resize_term(24, 80) # (nlines, ncols)

    tekst = 'sraaaaaaaam'

    # MAIN
    field1 = curses.newwin(1, 30, 0, 0)
    field2 = curses.newwin(1, 30, 1, 0)
    field1.addnstr(0, 0, tekst, 10, curses.A_REVERSE) 
    field1.refresh()
    field2.addnstr(0, 0, "Gunwooooo!", 10, curses.A_REVERSE) 
    field2.refresh()

    tekst = 'opodcieram'
    field1.refresh()
    sleep(2)
    # field.getch() # wait for keypress

def tui_wrapper():
    curses.wrapper(tui)

tui_thread = threading.Thread(target=tui_wrapper)
ksp_thread = threading.Thread(target=ksp)

tui_thread.start()
ksp_thread.start()



# curses.curs_set(visibility)
# curses.newwin(nlines, ncols, begin_y, begin_x)
# window.addnstr(y, x, str, n[, attr])