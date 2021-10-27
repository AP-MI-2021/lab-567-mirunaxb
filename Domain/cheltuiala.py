def create_cheltuiala(id, nr_ap, suma, data, tipul):
    '''

    :param nr_ap: int
    :param suma: int
    :param data: string (DD.MM.YYYY)
    :param tipul: string
    :return: Dictionar
    '''
    return [id, nr_ap, suma, data, tipul]

def get_id(cheltuiala):
    '''

    :param cheltuiala: Dictionar
    :return: nr_ap - int
    '''
    return cheltuiala[0]

def get_nr_ap(cheltuiala):
    '''

    :param cheltuiala: Dictionar
    :return: nr_ap - int
    '''
    return cheltuiala[1]

def get_suma(cheltuiala):
    '''

    :param cheltuiala: Dictionar
    :return: nr_ap - int
    '''
    return cheltuiala[2]

def get_data(cheltuiala):
    '''

    :param cheltuiala: Dictionar
    :return: data - string
    '''
    return cheltuiala[3]

def get_tipul(cheltuiala):
    '''

    :param cheltuiala: Dictionar
    :return: nr_ap - int
    '''
    return cheltuiala[4]


def to_str(cheltuiala):
    return f'Id ul cheltuielii este {get_id(cheltuiala)}, cu Nr_apartamentului {get_nr_ap(cheltuiala)}, suma {get_suma(cheltuiala)}, data {get_data(cheltuiala)} si tipul {get_tipul(cheltuiala)}'
