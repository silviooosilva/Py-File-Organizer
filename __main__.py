from consolemenu import ConsoleMenu
import colorama
from consolemenu.items import FunctionItem

from functions import *


class PyFileOrganizer:
    def __init__(self):
        pass

    def run(self):
        menu = ConsoleMenu("PyFileOrganizer", "Organize your files")

        start_item = FunctionItem("Start App", self.on_start_app)
        menu.append_item(start_item)

        info_item = FunctionItem("Info", self.on_info)
        menu.append_item(info_item)
        menu.show()

    def on_start_app(self):
        path = str(input('Paste the directory location: '))
        order(path)

    def on_info(self):
        print('« Go To : https://github.com/silviooosilva/Py-File-Organizer »')
        input('Tecle enter para continuar...')

#
# print(
#     f"""{colorama.Fore.WHITE}
#         ==========================
#         |Py - File Organizer 1.0 |
#         ==========================
#     """)
# print(
#         """
#         =====================
#         |        MENU       |
#         =====================
#         |[0] -  Start App   |
#         |[1] -  Info        |
#         |[2] -  Exit        |
#         |___________________|
#         """)
#
# option = int(input('>'))
#
# if(option == 0):
#     path = str(input('Paste the directory location: '))
#     order(path)
# elif(option == 1):
#     print('« Go To : https://github.com/silviooosilva/Py-File-Organizer »')
# elif(option == 2):
#     pass


if __name__ == '__main__':
    app = PyFileOrganizer()
    app.run()
    print("[!] Enjoy :) Bye")
    print(f'{colorama.Fore.YELLOW}By: Sílvio Silva')
