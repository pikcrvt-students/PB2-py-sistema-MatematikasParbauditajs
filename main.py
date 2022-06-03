'''
Izveidoja: Sidnijs Jurciks
Matemātikas Virkņu pārbaudes programma
'''
import os

def choose_task_type():
    atbilde = ''
    while atbilde != 'teorija' and atbilde != 'patstavigais darbs' and atbilde != 'parbaudes darbs':
        atbilde = input('Izvēlaties veidu - teorija, patstavigais darbs, parbaudes darbs ')
    return atbilde
def open_task_file(task_type):
    if task_type == 'teorija':
        opened_file = open('teorija.txt', 'r')
        data = opened_file.readlines()
        opened_file.close()
    elif task_type == 'patstavigais darbs':
        opened_file = open('patstavigie darbi.txt', 'r')
        data = opened_file.readlines()
        opened_file.close()
    else:
        opened_file = open('parbaudes darbi.txt', 'r')
        data = opened_file.readlines()
        opened_file.close()

    return data


def execute_task_file(task_file):
    print(task_file)
    return True

def begin():
    task_type = choose_task_type()
    task_file_text = open_task_file(task_type)
    if execute_task_file(task_file_text):
        os._exit()
    else:
        begin()

begin()

