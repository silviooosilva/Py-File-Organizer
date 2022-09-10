from colorama import Fore
from consolemenu import ConsoleMenu
from consolemenu.items import FunctionItem

from functions import order


class PyFileOrganizer:
    def __init__(self):
        pass

    @staticmethod
    def _wait_user():
        input('Tecle enter para continuar...')

    def run(self):
        menu = ConsoleMenu(f"{Fore.WHITE}PyFileOrganizer",
                           "Organize your files")

        start_item = FunctionItem("Start App", self.on_start_app)
        menu.append_item(start_item)

        info_item = FunctionItem("Info", self.on_info)
        menu.append_item(info_item)
        menu.show()

    def on_start_app(self):
        path = str(input('Paste the directory location: '))
        order(path)
        self._wait_user()

    def on_info(self):
        print('« Go To : https://github.com/silviooosilva/Py-File-Organizer »')
        self._wait_user()


if __name__ == '__main__':
    app = PyFileOrganizer()
    app.run()
    print("[!] Enjoy :) Bye")
    print(f'{Fore.YELLOW}By: Sílvio Silva')
