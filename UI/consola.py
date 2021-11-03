from Domain.cheltuiala import to_str
from Logic.crud import add_cheltuiala, edit_cheltuiala, delete_cheltuiala
from Logic.operatiuni import stergere_toate_cheltuieli

def print_meniu():
    print('''
    MENIU
    1. CRUD 
    2. Operatiuni
    3. Undo/Redo
    x. Iesire
    ''')

def print_crud_meniu():
    print('''
    MENIU Crud
    1. Adaugare
    2. Modificare
    3. Stergere
    4. Afisare toate cheltuielile
    5. Inapoi
    ''')

def print_operatiuni_meniu():
    print('''
    MENIU Operatiuni
    1. Stergerea tuturor cheltuielilor unui apartament dat.
    2. Afișarea tuturor prăjiturilor introduse începând cu un an dat.
    3. Determinarea prăjiturii cu cel mai mare număr de tipul din fiecare an al introducerii.
    4. Ordonarea prăjiturilor crescător după raportul preț / tipul.
    5. Afișarea sumelor prețurilor pentru fiecare an al introducerii.
    6. Inapoi
    ''')


def run_crud_ui(cheltuieli):
    '''

    :param cheltuieli: lista de cheltuieli
    :return:
    '''

    def handle_show_all(cheltuieli):
        '''
        Afisare lista de cheltuieli din memorie
        :param cheltuieli: lista de prajitur
        :return:
        '''
        for cheltuiala in cheltuieli:
            print(to_str(cheltuiala))

    def handle_edit_cheltuiala_ui(cheltuieli):
        '''
        Adaugam o cheltuiala citita de la tastatura in lista de cheltuieli
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        id = input('Dati idul cheltuielii pe care vreti sa o editati')
        nr_ap = input('Dati nr_aple')
        suma = input('Dati sumaa')
        data = input('Dati dataul')
        tipul = input('Dati numarul de tipul')
        try:
            cheltuieli = edit_cheltuiala(cheltuieli, id, nr_ap, suma, data, tipul)
            print('cheltuiala a fost modificata cu succes')
            return cheltuieli
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')

    def handle_delete_cheltuiala_ui(cheltuieli):
        '''
        Stergem cheltuieli din memorie
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        id_cheltuiala = input("Dati id-ul cheltuielii care se va sterge: ")
        cheltuieli_new = delete_cheltuiala(cheltuieli, id_cheltuiala)
        print("Stergerea a avut loc cu succes!")
        return cheltuieli_new

    def handle_add_cheltuiala_ui(cheltuieli):
        '''
        Adaugam o cheltuiala citita de la tastatura in lista de cheltuieli
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        id = input('Intorduceti ID-ul cheltuielii: ')
        nr_ap = input('Introduceti numarul apartamentului: ')
        suma = input('Introduceti suma: ')
        data = input('Introduceti data, pastrand formatul DD.MM.YY: ')
        tipul = input('Intoduceti tipul cheltuielii, alegand dintre "intretinere", "canal", "alte cheltuieli": ')
        try:
            cheltuieli = add_cheltuiala(cheltuieli, id, nr_ap, suma, data, tipul)
            print('cheltuiala a fost adaugata cu succes')
            return cheltuieli
        except ValueError as ve:
            print("!!! Au aparut erori")
            print(ve)
        except:
            print('Unknown error')
        finally:
            pass
            # codul de aici se executa si daca a fost functia executata cu succes si si daca au aparut erori

    while True:
        print_crud_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            cheltuieli = handle_add_cheltuiala_ui(cheltuieli)
        elif cmd == '2':
            cheltuieli = handle_edit_cheltuiala_ui(cheltuieli)
        elif cmd == '3':
            cheltuieli = handle_delete_cheltuiala_ui(cheltuieli)
        elif cmd == '4':
            handle_show_all(cheltuieli)
        elif cmd == '5':
            break
        else:
            print("Comanda invalida")


def run_operatiuni_ui(cheltuieli):
    '''

    :param cheltuieli: lista de cheltuieli
    :return:
    '''

    def handle_stergere_toate_cheltuieli(cheltuieli):
        '''
        Reducerea nr de tipul pentru cheltuielile ce contin un string dat de la tastatura
        Cu cat se reduc tipulle se citeste de asemenea de la tastatura
        :param cheltuieli: lista de cheltuieli
        :return:
        '''
        nr_ap = int(input("Dati numarul apartamentului unde vreti sa stergeti toate cheltuielile: "))
        cheltuieli = stergere_toate_cheltuieli(cheltuieli, nr_ap)
        print('Toate cheltuielile pentru apartamentul introdus au fost sterse cu succes!')
        return cheltuieli

    while True:
        print_operatiuni_meniu()
        cmd = input("Comanda: ")
        if cmd == '1':
            cheltuieli = handle_stergere_toate_cheltuieli(cheltuieli)
        elif cmd == '6':
            break
        else:
            print("Comanda invalida")



def run_undo_redo_ui(cheltuieli):
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
            run_undo_redo_ui(cheltuieli)
        elif cmd == 'x':
            print("La revedere!")
            break
        else:
            print('Comanda invalida')
