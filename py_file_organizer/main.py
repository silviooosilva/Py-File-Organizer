import argparse
import os
import sys
import threading

from colorama import Fore
# noinspection PyPackageRequirements
from consolemenu import ConsoleMenu
# noinspection PyPackageRequirements
from consolemenu.items import FunctionItem

if __package__ in {None, ''}:  # pragma: no cover - allow running as `python main.py`
    package_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if package_root not in sys.path:
        sys.path.insert(0, package_root)
    from py_file_organizer import functions  # type: ignore
else:  # pragma: no cover
    from . import functions  # type: ignore


def _parse_args(arguments=None):
    parser = argparse.ArgumentParser(
        description='Organize files into folders based on their extensions.'
    )
    parser.add_argument(
        'directory',
        nargs='?',
        help='Directory to organize. When omitted, the interactive menu is shown.',
    )
    parser.add_argument(
        '--background', '-b',
        action='store_true',
        help='Run the organization in the background (only when a directory is provided).',
    )
    return parser.parse_args(arguments if arguments is not None else [])


def _organize_directory(path: str, wait_callback=None):
    organizer = functions.PyFileOrganizer(path)
    if hasattr(organizer, '_check_dir') and not organizer._check_dir():
        if wait_callback is not None:
            wait_callback()
        return False
    organizer.run()
    if wait_callback is not None:
        wait_callback()
    return True


def _print_farewell():
    print("[!] Enjoy :) Bye")
    print(f'{Fore.YELLOW}By: Sílvio Silva')


def _start_background_job(path: str, wait_callback=None):
    thread = threading.Thread(
        target=_organize_directory,
        args=(path,),
        kwargs={'wait_callback': wait_callback},
        daemon=True,
    )
    thread.start()
    return thread


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
        self._add_background_item(menu)
        self._add_info_item(menu)

        menu.show()

    def _add_info_item(self, menu):
        info_item = FunctionItem("Info", self.on_info)
        menu.append_item(info_item)

    def _add_start_item(self, menu):
        start_item = FunctionItem("Start App", self.on_start_app)
        menu.append_item(start_item)

    def _add_background_item(self, menu):
        background_item = FunctionItem("Start App (background)",
                                       self.on_start_app_background)
        menu.append_item(background_item)

    def on_start_app(self):
        path = str(input('Paste the directory location: '))
        _organize_directory(path, wait_callback=self._wait_user)

    def on_start_app_background(self):
        path = str(input('Paste the directory location: '))
        _start_background_job(path)
        print(f"Started background organization for: {path}")
        self._wait_user()

    def on_info(self):
        print('« Go To : https://github.com/silviooosilva/Py-File-Organizer »')
        self._wait_user()


def main(argv=None):
    args = _parse_args(argv)
    if args.directory:
        if args.background:
            _start_background_job(args.directory)
            print(f"Started background organization for: {args.directory}")
            _print_farewell()
            return 0
        success = _organize_directory(args.directory)
        _print_farewell()
        return 0 if success else 1

    app = PyFileOrganizerUI()
    app.run()
    _print_farewell()
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
