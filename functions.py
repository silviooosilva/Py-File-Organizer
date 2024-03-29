############################
#                          #
#    By: Sílvio Silva      #
#        07/09/2022        #
############################
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
        if not os.path.isdir(dir):
            os.mkdir(dir)
    except:
        pass


def _move(arg1: list, arg2: list):
    try:
        shutil.move(arg1, arg2)
        return True
    except:
        return False

def verify_path(dir: str):
    try:
        if os.path.isdir(dir):
            return True
        return False
    except OSError:
        print(f'Lamentamos, mas não conseguimos realizar a operação desejada. Acompanhe o erro {OSError.args}')
def verify_file(file: str):
    try:
        if os.path.isfile(file):
            return True
        return False
    except OSError:
        print(f'Lamentamos, mas não conseguimos realizar a operação desejada. Acompanhe o erro {OSError.args}')

def list_path(dir: list):
    try:
        return [f for f in listdir(dir) if isfile(join(dir, f))]
    except OSError:
        print('Aconteceu um erro não programável. Tente novamente.')


def order(dir: str):
    tdd = 0
    keys = list(extensions.items())
    if(verify_path(dir)):
        
        for arquivo in list_path(dir):


            for count in range(len(extensions)):
                extension = "".join(get_extension(arquivo)[1]).lower()

                if(extension in keys[count][1]):
                    create_dir(keys[count][0], dir)
                    all = "".join(get_extension(arquivo))


                    if(verify_file(f"{keys[count][0]}")):
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


