from time import sleep
from selenium import webdriver
import GithubAutomation
import curses

options = [' Create New ', ' List Repos ', ' Delete Repo ', ' Add Credentials ', ' Exit ']

def print_menu(stdscr, current_selection):
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
    stdscr = curses.initscr()
    y, x = stdscr.getmaxyx()
    for idx, i in enumerate(options):
        if(current_selection == idx+1):
            stdscr.attron(curses.color_pair(1))
            stdscr.addstr(y//2+idx-3, x//2 -(len(i)//2), i)    
            stdscr.attroff(curses.color_pair(1))
            continue
        stdscr.addstr(y//2+idx-3, x//2 -(len(i)//2), i)
    stdscr.refresh()

def main(stdscr):

    stdscr = curses.initscr()
    curses.curs_set(0)
    current_selection = 1

    y, x = stdscr.getmaxyx()

    logo = open('./src/Logo').read()
    for idx, i in enumerate(logo.split('\n')):
        stdscr.addstr(idx+y//2-11, x//2-24, i)
    stdscr.refresh()
    sleep(1.5)
    stdscr.clear()
    
    while(1):
        print_menu(stdscr, current_selection)
        key = stdscr.getch()
        if(key == curses.KEY_UP and current_selection>1):
            current_selection-=1
        elif(key == curses.KEY_DOWN and current_selection<5):
            current_selection+=1
        elif(key == curses.KEY_ENTER or key in [10, 13]):
            if(current_selection == 1):
                GithubAutomation.CreateRepo(stdscr)
            if(current_selection == 2):
                GithubAutomation.ListRepo(stdscr)
            if(current_selection == 4):
                GithubAutomation.AddCredentials(stdscr)
            if(current_selection == 5):
                exit()
            
curses.wrapper(main)
