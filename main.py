# import start

import colored, fade, rich, requests, random, os, colorama, names, asyncio

from colored import fore as f, style as st, fg
from colorama import init, Fore
from rich.console import Console
from rich import print as p
from requests import request
from string import ascii_lowercase, ascii_uppercase, digits
from login import username
os.system('echo "export COLORTERM=truecolor" >> .zshrc')
# import end


c = Console(
        color_system="auto", 
        legacy_windows=True,
      # soft_wrap=True
    )


# -----ACCOUNT CONFIGURATION

def namegen(size):
    return "".join([random.choice(ascii_lowercase + ascii_uppercase + digits) for i in
    range(size)])
ig_username = namegen(10)

def passgen(size):
    return "".join([random.choice(ascii_lowercase + ascii_uppercase + digits) for i in
    range(size)])
ig_password = passgen(14)    

def fnamegen():
    fname = names.get_first_name()
    return    
# -----ACCOUNT CONFIGURATION

# -----ESSENTIALS
def clear():
    os.system("clear" if os.name != "nt" else "cls")
# -----ESSENTIALS

# -----ASCII PART

def splashbanner():
    clear()
    init(strip=True, convert=True, autoreset=True)
    colors = [fade.greenblue, fade.purpleblue, fade.purplepink, fade.water, fade.pinkred]
    splash = (f'''
                ███████╗██████╗  █████╗ ██╗   ██╗██████╗
                ██╔════╝██╔══██╗██╔══██╗██║   ██║██╔══██╗
                █████╗  ██████╔╝███████║██║   ██║██║  ██║
                ██╔══╝  ██╔══██╗██╔══██║██║   ██║██║  ██║
                ██║     ██║  ██║██║  ██║╚██████╔╝██████╔╝
                ╚═╝     ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ 
                v2.0 (rewritten)
                made by hate#1337 | with love ♡
                Logged in as: {username}
''')

    c.print(fade.pinkred(splash), justify="center")
    colorama.deinit()
def selections():
    print(f'{f.WHITE}[{f.MAGENTA_2A}{st.BOLD}1{f.WHITE}{st.RESET}] - Open Account Creator')
    print(f'{f.WHITE}[{f.MAGENTA_2A}{st.BOLD}2{f.WHITE}{st.RESET}] - Open Account Follower')
    print(f'{f.WHITE}[{f.MAGENTA_2A}{st.BOLD}3{f.WHITE}{st.RESET}] - Open Account Reporter')
    print(f'{f.WHITE}[{f.MAGENTA_2A}{st.BOLD}4{f.WHITE}{st.RESET}] - Open Post Liker')
    print(f'{f.WHITE}[{f.MAGENTA_2A}{st.BOLD}5{f.WHITE}{st.RESET}] - Open Rapist Settings \n\n')
    print(f'{f.WHITE}[{f.MAGENTA_2A}{st.BOLD}6{f.WHITE}{st.RESET}] - Open Developer Panel \n')

def anykeytocontinue():
    color = fg('#6a58f5')
    key = input(color + "Press any key to continue..")
    splashbanner()
    selections()
    getanswer()

def getanswer():
    init(strip=True, convert=True, autoreset=True)
    answer = input(f'{f.MAGENTA_2A}{st.BOLD}Your Option: {st.RESET}{f.WHITE}')
    if answer in ("1", "2", "3", "4", "5", "6"):
        print(answer)
    else:
        #clear()
        color = fg("#ff1c42")
        p(color + f"Please Provide an opinion from the list above.")
        anykeytocontinue()
# ----- ASCII PART

# ----- SCRIPT START

def creation():
    while True:
        payload = {
    'email': "",
    'password': ig_password,
     'username': ig_username,
    'first_name': "hi",# fname,
    'client_id': 'W6mHTAAEAAHsVu2N0wGEChTQpTfn',
    'seamless_login_enabled': '1',
    'gdpr_s': '%5B0%2C2%2C0%2Cnull%5D',
    'tos_version': 'eu',
    'opt_into_one_tap': 'false'
}

        url = "https://www.instagram.com/accounts/web_create_ajax/"
        r = requests.post(url, json=payload)
        namegen() 
        passgen()
        fnamegen()

# -----SCRIPT

# r = requests.post(url, json=payload)
splashbanner()
selections()
getanswer()