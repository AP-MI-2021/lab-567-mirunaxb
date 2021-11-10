from copy import deepcopy

from Domain.cheltuiala import *
from Logic.validator import validate_cheltuiala

def find_cheltuiala(cheltuieli, id):
    '''
    Find cheltuiala in cheltuieli with id
    If not found, we return None
    :param cheltuieli:
    :param id:
    :return:
    '''
    for cheltuiala in cheltuieli:
        if get_id(cheltuiala) == id:
            return cheltuiala
    return None

def add_cheltuiala(cheltuieli, id, nr_ap, suma, data, tipul, undo_lst, redo_lst):
    '''
    Adaugam in memorie, in lista de cheltuieli o cheltuiala formata
    din fieldurile: id, nr_ap, suma, data, tipul, an_introducere
    :param cheltuieli: lista de cheltuieli
    :param id: string
    :param nr_ap: string
    :param suma: string
    :param data: string
    :param tipul: string
    :return:
    '''

    id, nr_ap, suma, data, tipul = validate_cheltuiala(id, nr_ap, suma, data, tipul)
    cheltuiala = create_cheltuiala(id, nr_ap, suma, data, tipul)
    undo_lst.append(cheltuieli)
    redo_lst.clear()
    return cheltuieli + [cheltuiala]

def edit_cheltuiala(cheltuieli, id, nr_ap_new, suma_new, data_new, tipul_new, undo_lst, redo_lst):
    '''
    Editarea cheltuieli cu idul id si aruncarea unei erori ValueError in cazul in care fieldurile nu sunt
    corecte
    :param cheltuieli:
    :param id:
    :param nr_ap_new:
    :param suma_new:
    :param data_new:
    :param tipul_new:
    :return:
    '''
    id, nr_ap_new, suma_new, data_new, tipul_new = validate_cheltuiala(id, nr_ap_new, suma_new, data_new, tipul_new)
    updated_list = deepcopy(cheltuieli)
    for cheltuiala in updated_list:
        if get_id(cheltuiala) == id:
            set_nr_ap(cheltuiala, nr_ap_new)
            set_suma(cheltuiala, suma_new)
            set_data(cheltuiala, data_new)
            set_tipul(cheltuiala, tipul_new)
    undo_lst.append(cheltuieli)
    redo_lst.clear()
    return updated_list

def delete_cheltuiala(cheltuieli, id, undo_lst, redo_lst):
    '''
    :param cheltuieli:
    :param id:
    :return:
    '''
    result_list = []
    for cheltuiala in cheltuieli:
        if get_id(cheltuiala) != id:
            result_list.append(cheltuiala)
    undo_lst.append(cheltuieli)
    redo_lst.clear()
    return result_list
