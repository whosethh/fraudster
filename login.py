# import start

import colored, fade, rich, requests, random, os, colorama, names, asyncio

from colored import fore as f, style as st, fg
from colorama import init, Fore
from rich.console import Console
from rich import print as p
from requests import request
from getpass import getpass
import sqlite3, aiosqlite
from main import splashbanner, clear, passgen, fnamegen, getanswer, selections, namegen
os.system('echo "export COLORTERM=truecolor" >> .zshrc')
# import end


c = Console(
        color_system="auto", 
        legacy_windows=True,
      # soft_wrap=True
    )


def clear():
    os.system("clear" if os.name != "nt" else "cls")

def splash():
    clear()
    init(strip=True, convert=True, autoreset=True)
    splash = ('''
                ███████╗██████╗  █████╗ ██╗   ██╗██████╗
                ██╔════╝██╔══██╗██╔══██╗██║   ██║██╔══██╗
                █████╗  ██████╔╝███████║██║   ██║██║  ██║
                ██╔══╝  ██╔══██╗██╔══██║██║   ██║██║  ██║
                ██║     ██║  ██║██║  ██║╚██████╔╝██████╔╝
                ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
                v2.0 (rewritten)
                made by hate#1337 | with love ♡
                Authorization Screen 
    ''')
    c.print(fade.greenblue(splash), justify="center")

async def login():
    color = fg('#42ff94')
    color2 = fg('#42c0ff')
    color3 = fg('#fc5353')
    color4 = fg('#faf273')
    username = input(color + "Please Provide Your Username: ")
    password = getpass(color2 + "Please Provide Your password: ")
    database = await aiosqlite.connect("./credentials.db")
    cursor = database.cursor()
    await cursor.execute("""
    SELECT * FROM users
    WHERE username = ? AND password = ?
    """, (username, password,))
    exists = cursor.fetchone()
    if exists:
        print(color4 + f"Welcome back {username}")
        asyncio.sleep(4)
        splashbanner()
    else:
        print(color3 + f"Sorry, you're not listed in the database.")
        asyncio.sleep(4)
        splash()

splash()
asyncio.run(login())