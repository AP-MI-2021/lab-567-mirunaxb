from Domain.cheltuiala import get_nr_ap, get_data, get_id, get_suma, get_tipul, create_cheltuiala


def stergere_toate_cheltuieli(cheltuieli, nr_ap_stergere):
    '''
    Stergerea tuturor cheltuielilor pentru un apartament ales.
    :param cheltuieli: lista
    :param nr_ap_stergere: int
    :return:
    '''
    result = []
    for cheltuiala in cheltuieli:
        if get_nr_ap(cheltuiala) != nr_ap_stergere:
            result.append(cheltuiala)
    if len(result) == len(cheltuieli):
        raise ValueError('Nu exista nici o cheltuiala pentru acest apartament.')
    return result

def add_value(cheltuieli, data_cautata, val):
    '''
    Adaugare valoare (la suma) tuturor cheltuielilor pentru o data aleasa.
    :param cheltuieli: lista
    :param data_cautata: string
    :param val: float
    :return:
    '''
    result = []
    for cheltuiala in cheltuieli:
        if get_data(cheltuiala) == data_cautata:
            cheltuiala_new = create_cheltuiala(get_id(cheltuiala), get_nr_ap(cheltuiala), float(get_suma(cheltuiala)) +
                                               val, get_data(cheltuiala), get_tipul(cheltuiala))
            result.append(cheltuiala_new)
        else:
            result.append(cheltuiala)
    return result

def sort_cheltuieli(cheltuieli):
    '''
    Sortare cheltuieli descrescator
    :param cheltuieli: lista
    :return:
    '''
    return sorted(cheltuieli, key = lambda cheltuiala: get_suma(cheltuiala), reverse = True)

def sorting_criteria(cheltuiala):
    '''
    :param cheltuiala:
    :return:
    '''
    return get_suma(cheltuiala)