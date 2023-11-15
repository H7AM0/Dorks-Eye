import sys,time,random
from googlesearch import search # google



CYAN = "\033[36m"
RED = "\033[91m"
RED2 = "\033[1;31m"
GREEN = "\033[1;32m"
BLUE2 = "\033[34m"
BLUE = "\033[94m"
PURPLE = "\033[1;95m"
YELLOW = "\033[1;33m"
RESET_COLOR = "\033[0m"


def hamo_logo(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.009)

logo = (f'''{RESET_COLOR}



    ░░░░░▄▄▀▀▀▀▀▀▀▀▀▄▄░░░░░
    ░░░░█░░░░░░░░░░░░░█░░░░
    ░░░█░░░░░░░░░░▄▄▄░░█░░░
    ░░░█░░▄▄▄░░▄░░███░░█░░░
    ░░░▄█░▄░░░▀▀▀░░░▄░█▄░░░
    ░░░█░░▀█▀█▀█▀█▀█▀░░█░░░ 
    ░░░▄██▄▄▀▀▀▀▀▀▀▄▄██▄░░░
    ░▄█░█▀▀█▀▀▀█▀▀▀█▀▀█░█▄░
    {CYAN}░░░╔╗╔╗╔══╗╔═╦═╗╔═╗░░░░ {RED2}Author : {RESET_COLOR}Mohamed Ahmed Amer | Hamo
    {CYAN}░░░║╚╝║║╔╗║║║║║║║║║░░░░ {GREEN}Github : {RESET_COLOR}https://github.com/H7AM0
    {CYAN}░░░║╔╗║║╠╣║║║║║║║║║░░░░ {BLUE2}Telegram : {RESET_COLOR}https://t.me/hamo_back
    {CYAN}░░░╚╝╚╝╚╝╚╝╚╩═╩╝╚═╝░░░░ {BLUE2}Instagram : {RESET_COLOR}https://instagram.com/4.4cq/''')


hamo_logo(logo)

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.0025)

lol = str("=" * 65)
jalan(f"{RED}  {lol}")

DORKS_EYE = (f"""{BLUE}
 ▓█████▄  ▒█████   ██▀███   ██ ▄█▀  ██████    ▓█████▓██   ██▓▓█████
 ▒██▀ ██▌▒██▒  ██▒▓██ ▒ ██▒ ██▄█▒ ▒██    ▒    ▓█   ▀ ▒██  ██▒▓█   ▀
 ░██   █▌▒██░  ██▒▓██ ░▄█ ▒▓███▄░ ░ ▓██▄      ▒███    ▒██ ██░▒███
 ░▓█▄   ▌▒██   ██░▒██▀▀█▄  ▓██ █▄   ▒   ██▒   ▒▓█  ▄  ░ ▐██▓░▒▓█  ▄
 ░▒████▓ ░ ████▓▒░░██▓ ▒██▒▒██▒ █▄▒██████▒▒   ░▒████▒ ░ ██▒▓░░▒████▒
 ▒▒▓  ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░   ░░ ▒░ ░  ██▒▒▒ ░░ ▒░ ░
 ░ ▒  ▒   ░ ▒ ▒░   ░▒ ░ ▒░░ ░▒ ▒░░ ░▒  ░ ░    ░ ░  ░▓██ ░▒░  ░ ░  ░
 ░ ░  ░ ░ ░ ░ ▒    ░░   ░ ░ ░░ ░ ░  ░  ░        ░   ▒ ▒ ░░     ░
 ░        ░ ░     ░     ░  ░         ░        ░  ░░ ░        ░  ░
 ░                                                  ░ ░   """)
jalan(DORKS_EYE)


DORK = input(f" {BLUE2}[?]{GREEN} Enter the dork search query {PURPLE}->{YELLOW} ")
try:
    AMOUNT = int(input(f" {BLUE2}[?]{GREEN} Enter the number of websites to display {PURPLE}->{YELLOW} "))
except:
    exit(f' {BLUE2}[!] {RED}This input supports numbers only')
filename = input(f" {BLUE2}[?]{GREEN} Enter the file name {PURPLE}->{YELLOW} ")
if '.txt' not in filename:
    filename = f'{filename}.txt'
print()
jalan(f"{RED}  {lol}")
print()

numb = 0

for result in search(DORK, tld="com", lang="en", num=AMOUNT, start=0, stop=None, pause=2):
    numb += 1
    color = random.choice([CYAN,GREEN,BLUE,PURPLE,YELLOW,RESET_COLOR])
    print (f" {BLUE2}[{numb}] {color}{result}")
    time.sleep(0.1)
    data = (f" [{numb}] {result} \n")
    file = open(filename, "a")
    file.write(str(data))
    file.close()
    if numb >= int(AMOUNT):
        break
    time.sleep(0.1)



print()
jalan(f"{RED}  {lol}")
print()
input(F' {BLUE2}[!] {YELLOW} The file has been completed and saved in {RESET_COLOR}{filename} \n {BLUE2}[?]{GREEN} Press Enter to close {PURPLE}->{YELLOW} ')
hamo_logo(logo)
exit(f'{RESET_COLOR}')