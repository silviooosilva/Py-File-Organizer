import colorama
from functions import *

print(
    f"""{colorama.Fore.WHITE}
        ==========================
        |Py - File Organizer 1.0 |
        ==========================
    """)
print(
        """
        =====================
        |        MENU       |
        =====================
        |[0] -  Start App   |
        |[1] -  Info        |
        |[2] -  Exit        |
        |___________________|
        """)

option = int(input('>'))
if(option == 0):
    path = str(input('Paste the directory location: '))
    order(path)
elif(option == 1):
    print('« Go To : https://github.com/silviooosilva/Py-File-Organizer »')
elif(option == 2):
    pass
print("[!] Enjoy :) Bye")
print(f'{colorama.Fore.YELLOW}By: Sílvio Silva')