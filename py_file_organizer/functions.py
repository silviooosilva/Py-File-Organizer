"""
By: Sílvio Silva
   07/09/2022
"""

import os
import shutil
from os import listdir
from os.path import isfile, join

from colorama import Fore

from py_file_organizer.extensions import extensions


class PyFileOrganizer:
    def __init__(self, directory: str, dryrun: bool = True):
        self.directory = directory

    def _check_dir(self):
        if not os.path.isdir(self.directory):
            print(f'{Fore.RED} The Directory {self.directory} '
                  f'Does not exist. Try Again [!]')
            return False
        return True

    def run(self):
        try:
            if not self._check_dir():
                return
            self._create_organization_dirs()
            self._order()
        except Exception as e:
            print(f'{Fore.RED} Error: {e.__class__.__name__} - {e}')

    @staticmethod
    def get_extension(path: str):
        """
        Função para pegar as extensões dos arquivos
        """
        return os.path.splitext(path)[1].lower()

    def _create_dir(self, directory: str):
        """
        Função para criar os diretórios onde serão organizados os arquivos
        """
        os.chdir(self.directory)
        if not os.path.isdir(directory):
            os.mkdir(directory)

    @staticmethod
    def _move(arg1, arg2):
        shutil.move(arg1, arg2)

    def _order(self):
        onlyfiles = self._get_files()
        tdd = self._process_files(onlyfiles)
        self._show_result_message(tdd)

    def _process_files(self, onlyfiles):
        tdd = 0
        for arquivo in onlyfiles:
            tdd += self._process_file(arquivo)
        return tdd

    @staticmethod
    def _show_result_message(tdd):
        if tdd > 0:
            print(f"{Fore.GREEN}Organization made with success[!]")
        else:
            print(f"{Fore.YELLOW}This dir is already organizaded[!]")

    def _process_file(self, arquivo):
        extension = self.get_extension(arquivo)
        target_dir = self._get_target_dir(extension)
        if target_dir is None or os.path.isfile(f"{target_dir}"):
            return 0

        self._move(arquivo, target_dir)

        return 1

    @staticmethod
    def _get_target_dir(extension):
        for dirname, exts in extensions.items():
            if extension in exts:
                return dirname
        return None

    def _get_files(self):
        onlyfiles = [f for f in listdir(self.directory)
                     if isfile(join(self.directory, f))]
        return onlyfiles

    def _create_organization_dirs(self):
        for dirname, exts in extensions.items():
            self._create_dir(dirname)
