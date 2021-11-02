def validate_cheltuiala(id, nr_ap, suma, data, tipul):
    '''
    Validate params for a cheltuiala/cake
    Throws a ValueError if fields are not correct
    :param id:
    :param nr_ap:
    :param suma:
    :param data:
    :param tipul:
    :return:
    '''
    errors = []
    if id == '':
        errors.append('Id-ul nu poate fi vid')
    if nr_ap == '':
        errors.append('Numar apartamentului nu poate fi vid')

    try:
        suma = float(suma)
        if suma < 0:
            errors.append('Suma trebuie sa fie un numar pozitiv')
    except ValueError:
        errors.append('Suma trebuie sa fie un numar real')

    if data == '':
        errors.append('Data nu poate fi vida')
    if tipul == '':
        errors.append('Tipul nu poate fi vid')

    if len(errors) != 0:
        raise ValueError(errors)

    return id, nr_ap, suma, data, tipul
