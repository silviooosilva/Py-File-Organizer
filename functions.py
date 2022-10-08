############################
#                          #
#    By: Sílvio Silva      #
#        07/09/2022        #
############################
from calendar import c
import os
import platform
import shutil
from extensions import extensions
from colorama import *
from os import listdir
from os.path import isfile, join



    # Função para limpar a tela após a inicialização 

def clear_screen():

    if "windows" in platform.system().lower():
        command = 'cls'
    else:
        command = 'clear'
    os.system(command)


clear_screen()


# Função para pegar as extensões dos arquivos

def get_extension(path: list):
    try:
        split_name = os.path.splitext(path)
        return split_name
    except OSError:
        print(f'{Fore.RED} Não Foi Possível executar a função! Tente Novamente [!]')


# Função para criar os diretórios onde serão organizados os arquivos
def create_dir(dir: list, location: str):
    try:
        os.chdir(location)
        if os.path.isdir(dir):
            pass
        else:
            os.mkdir(dir)
    except:
        pass


def create_main_dir(location: str):
    os.chdir(location)
    path = 'Py-File-Organizer'

    try:
        if(os.path.isdir(path)):
            pass
        else:
            os.mkdir(path)
    except OSError:
        print(f'{Fore.RED} Não foi possível criar o diretório mãe! Tente novamente [!]')




def _move(arg1: list, arg2: list):
    try:
        shutil.move(arg1, arg2)
        return True
    except:
        return False





def order(dir: str):
    # path = 'Py-File-Organizer'
    # create_main_dir(dir)
    tdd = 0
    keys = list(extensions.items())
    if(os.path.isdir(dir)):
        onlyfiles = [f for f in listdir(dir) if isfile(join(dir, f))]
        for arquivo in onlyfiles:
            for count in range(len(extensions)):
                extension = "".join(get_extension(arquivo)[1]).lower()
                if(extension in keys[count][1]):
                    create_dir(keys[count][0], dir)
                    # print(keys[count][1])
                    all = "".join(get_extension(arquivo))
                    if(os.path.isfile(f"{keys[count][0]}")):
                        pass
                    else:
                                    
                        if(_move(all, f'{keys[count][0]}')):
                            tdd = tdd + 1
                        else:
                            print('Something went wrong! Try Again.')

        if(tdd > 0):
            print(f"{Fore.GREEN}Organization made with success[!]")
            
        if(tdd == 0):
            print(f"{Fore.YELLOW}This dir is already organizaded[!]")
    else:
            print(f'{Fore.RED} The Directory {dir} Does not exist. Try Again [!]')



# print(f"{Fore.RED}Aconteceu um erro não programável. Tente Novamente [!]")

