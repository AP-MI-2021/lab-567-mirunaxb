from Domain.cheltuiala import *
from Logic.crud import *

def print_meniu():
    print('''
    MENIU:
    1. CRUD
    2. Operatiuni
    3. Undo/REDO
    x. Iesire
    ''')

def print_crud_meniu():
    print('''
    MENIU CRUD:
    1. Adaugare
    2. Modificare
    3. Stergere
    x. Afisare toate
    b. Inapoi
    ''')

def handle_show_all(cheltuieli):
    '''
    Afisare lista de cheltuieli din memorie
    :param cheltuieli: lista de cheltuieli
    :return:
    '''
    for cheltuiala in cheltuieli:
        print(to_str(cheltuiala))

def handle_add_cheltuiala_ui(cheltuieli):
    id_ap = int(input('Introduceti id-ul cheltuielii aici: '))
    nr_ap = int(input('Introduceti numarul apartamentului aici: '))
    suma = int(input('Introduceti suma cheltuielii aici: '))
    data = input('Introduceti data in care s - a emis cheltuiala in format DD.MM.YYYY aici: ')
    tip = input('Introduceti tipul cheltuielii aici: ')
    # new_cheltuiala = create_cheltuiala(id_ap, nr_ap, suma, data, tip)
    cheltuieli = adaugare(cheltuieli, id_ap, nr_ap, suma, data, tip)
    return cheltuieli

def handle_modify_cheltuiala_ui(cheltuieli):
    id_ap = int(input('Introduceti id-ul cheltuielii care doriti sa se modifice: '))
    nr_ap = int(input('Dati numarul apartamentului al cheltuielii care se actualizeaza: '))
    suma = int(input('Dati aici noua suma a cheltuielii: '))
    data = input('Dati aici noua data a cheltuielii: ')
    tip = input('Dati aici noul tip al cheltuielii: ')
    new_cheltuiala = create_cheltuiala(id_ap, nr_ap, suma, data, tip)
    return modif(cheltuieli, new_cheltuiala)

def handle_delete_cheltuiala_ui(cheltuieli):
    id_ap = int(input('Dati aici id-ul cheltuielii care doriti sa se modifice: '))
    cheltuieli = stergere(cheltuieli, id_ap)
    print("S-a sters cu succes cheltuiala!")
    return cheltuieli

def run_crud_ui(cheltuieli):
    '''

    :param cheltuieli: lista de cheltuieli
    :return:
    '''
    while True:
        print_crud_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            handle_add_cheltuiala_ui(cheltuieli)
        if cmd == '2':
            handle_modify_cheltuiala_ui(cheltuieli)
        if cmd == '3':
            handle_delete_cheltuiala_ui(cheltuieli)
        elif cmd == 'x':
            handle_show_all(cheltuieli)
        elif cmd == 'b':
            break
        else:
            print("Comanda invalida")
    return cheltuieli

def run_operatiuni_ui(cheltuieli):
    pass
def run_undo_ui(cheltuieli):
    pass

def run_console(cheltuieli):
    '''
    :param cheltuieli: lista de cheltuieli
    :return:
    '''
    while True:
        print_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            run_crud_ui(cheltuieli)
        elif cmd == '2':
            run_operatiuni_ui(cheltuieli)
        elif cmd == '3':
            run_undo_ui(cheltuieli)
        elif cmd == 'x':
            break
        else:
            print("Comanda invalida.")
    return cheltuieli