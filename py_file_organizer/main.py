from colorama import Fore
# noinspection PyPackageRequirements
from consolemenu import ConsoleMenu
# noinspection PyPackageRequirements
from consolemenu.items import FunctionItem

from py_file_organizer.functions import PyFileOrganizer


class PyFileOrganizerUI:
    def __init__(self):
        pass

    @staticmethod
    def _wait_user():
        input('Tecle enter para continuar...')

    def run(self):
        menu = ConsoleMenu(f"{Fore.WHITE}PyFileOrganizer",
                           "Organize your files")

        self._add_start_item(menu)
        self._add_info_item(menu)

        menu.show()

    def _add_info_item(self, menu):
        info_item = FunctionItem("Info", self.on_info)
        menu.append_item(info_item)

    def _add_start_item(self, menu):
        start_item = FunctionItem("Start App", self.on_start_app)
        menu.append_item(start_item)

    def on_start_app(self):
        path = str(input('Paste the directory location: '))
        organizer = PyFileOrganizer(path)
        organizer.run()
        self._wait_user()

    def on_info(self):
        print('« Go To : https://github.com/silviooosilva/Py-File-Organizer »')
        self._wait_user()


def main():
    app = PyFileOrganizerUI()
    app.run()
    print("[!] Enjoy :) Bye")
    print(f'{Fore.YELLOW}By: Sílvio Silva')


if __name__ == '__main__':
    main()
