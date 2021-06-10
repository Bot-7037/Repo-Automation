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


def ListRepo(stdscr):
    URL='https://api.github.com/users/Bot-7037/repos'
    lics = ["Apache License 2.0",
    "GNU General Public License v3.0",
    "MIT License",
    'BSD 2-Clause "Simplified" License',
    'BSD 3-Clause "New" or "Revised" License',
    "Boost Software License 1.0",
    "Creative Commons Zero v1.0 Universal",
    "Eclipse Public License 2.0",
    "GNU Affero General Public License v3.0",
    "GNU General Public License v2.0",
    "GNU Lesser General Public License v2.1",
    "Mozilla Public License 2.0",
    "The Unlicense"]

    y, x = stdscr.getmaxyx()
    stdscr.clear()
    _ = 'FETCHING'
    stdscr.addstr(y//2, x//2-len(_)//2, _)
    stdscr.refresh()
    from bs4 import BeautifulSoup
    import requests
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    soup = str(soup).split(',')

    repoList=[]
    for i in soup:
        if('"name"' in i):
            repoName = i.split(':')[1]
            repoName = repoName[1:-1]
            if(repoName in lics): continue
            repoList.append(repoName)
    
    stdscr.clear()
    for idx,i in enumerate(repoList):
        stdscr.addstr(y//2 - len(repoList)//2 +idx, x//2 - len(i)//2, i)
    stdscr.refresh()
    stdscr.getch()
    stdscr.clear()
    stdscr.refresh()
