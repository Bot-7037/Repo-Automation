import curses
import os
from time import sleep
from selenium import webdriver

def CreateRepo(stdscr):
    file = open('./src/credentials','r').read()
    stdscr.clear()
    username = file.split()[0]
    password = file.split()[1]

    stdscr.clear()
    y, x = stdscr.getmaxyx()
    _ = "Enter repository name"
    repoName=""
    stdscr.addstr(y//2, x//2 - len(_)//2, _)
    stdscr.refresh()

    while(1):
        key = stdscr.getch()
        if(key == curses.KEY_ENTER or key in [10,13]):
            break
        if(key == curses.KEY_BACKSPACE or key in [127, '\b', 8]):
            if(len(repoName) <2):
                repoName = ""
            else:
                repoName = repoName[:-1]
            stdscr.clear()
            stdscr.addstr(y//2, x//2 - len(_)//2, _)
            stdscr.addstr(y//2+1, x//2 - len(repoName)//2, repoName)
            stdscr.refresh()
            continue

        repoName+= chr(key)
        stdscr.clear()
        stdscr.addstr(y//2, x//2 - len(_)//2, _)
        stdscr.addstr(y//2+1, x//2 - len(repoName)//2, repoName)
        stdscr.refresh()

    driver = webdriver.Chrome(os.getcwd()+'\chromedriver.exe')

    # Access GitHub Login Page
    driver.get("https://github.com/new")

    # Log in to GitHub
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("login_field").send_keys(username)
    driver.find_element_by_name("commit").click()

    # Create New Repository
    driver.find_element_by_id("repository_name").send_keys(repoName)
    driver.find_element_by_xpath("//*[@id='new_repository']/div[4]/button").click()

    exit()

def AddCredentials(stdscr):
    stdscr.clear()
    y, x = stdscr.getmaxyx()
    _ = "Enter Username"
    username=""
    stdscr.addstr(y//2, x//2 - len(_)//2, _)
    stdscr.refresh()

    while(1):
        key = stdscr.getch()
        curses.curs_set(1)
        if(key == curses.KEY_ENTER or key in [10,13]):
            break
        if(key == curses.KEY_BACKSPACE or key in [127, '\b', 8]):
            if(len(username) <2):
                username = ""
            else:
                username = username[:-1]
            stdscr.clear()
            stdscr.addstr(y//2, x//2 - len(_)//2, _)
            stdscr.addstr(y//2+1, x//2 - len(username)//2, username)
            stdscr.refresh()
            continue
        username+= chr(key)
        stdscr.clear()
        stdscr.addstr(y//2, x//2 - len(_)//2, _)
        stdscr.addstr(y//2+1, x//2 - len(username)//2, username)
        stdscr.refresh()
    curses.curs_set(0)
    username += ' '

    stdscr.clear()
    _ = "Enter Password"
    password=""
    stdscr.addstr(y//2, x//2 - len(_)//2, _)
    stdscr.refresh()

    while(1):
        key = stdscr.getch()
        if(key == curses.KEY_ENTER or key in [10,13]):
            break
        if(key == curses.KEY_BACKSPACE or key in [127, '\b', 8]):
            if(len(password) <2):
                password = ""
            else:
                password = password[:-1]
            continue
        username+= chr(key)
        stdscr.addstr(y//2, x//2 - len(_)//2, _)
        stdscr.refresh()
    
    file = open('./src/credentials', "w")
    cred = username + password
    file.write(cred)
    file.close()