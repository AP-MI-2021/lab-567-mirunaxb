from Domain.cheltuiala import *
from Logic.crud import delete_cheltuiala


def stergere_toate_cheltuieli(cheltuieli, nr_ap_stergere):
    '''
    Reducerea tipullor cheltuielilor care au in nr_ap string_de_cautare
    :param cheltuieli: lista de cheltuieli
    :param string_de_cautare: string
    :param reducere: int
    :return:
    '''
    result_list = []
    for cheltuiala in cheltuieli:
        if get_nr_ap(cheltuiala) != nr_ap_stergere:
            result_list.append(cheltuiala)
    return result_list


def sort_cheltuieli(cheltuieli):
    pass
    #'''
    #:param cheltuieli:
    #:return:
    #'''
    # return sorted(cheltuieli, key=sorting_criteria)
    #return sorted(cheltuieli, key = lambda cheltuiala: get_data(cheltuiala)/get_tipul(cheltuiala))

def sorting_criteria(cheltuiala):
    pass
    #'''
    #:param cheltuiala:
    #:return:
    #'''
    #return get_data(cheltuiala)/get_tipul(cheltuiala)