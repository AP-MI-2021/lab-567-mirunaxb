from Logic.crud import *
from Logic.operatiuni import stergere_toate_cheltuieli, add_value
from Domain.cheltuiala import create_cheltuiala


def test_stergere_toate_cheltuieli():
    cheltuieli = []
    cheltuieli = add_cheltuiala(cheltuieli, 'id1', 1, 120.9, '04.06.2002', 'alte cheltuieli')
    cheltuieli = add_cheltuiala(cheltuieli, 'id2', 4, 120.9, '04.07.2002', 'alte cheltuieli')
    cheltuieli = add_cheltuiala(cheltuieli, 'id3', 4, 145.8, '04.07.2002', 'alte cheltuieli')
    assert len(cheltuieli) == 3
    cheltuieli = stergere_toate_cheltuieli(cheltuieli, 4)
    assert len(cheltuieli) == 1

def test_add_value():
    cheltuieli = []
    cheltuieli = add_cheltuiala(cheltuieli, 1, 4, 154.35, "23.06.2021", "alte cheltuieli")
    cheltuieli = add_cheltuiala(cheltuieli, 2, 35, 400, "04.06.2002", "intretinere")
    cheltuieli = add_cheltuiala(cheltuieli, 3, 124, 98.5, "04.06.2002", "canal")

    cheltuieli = add_value(cheltuieli, "04.06.2002", 10)
    assert len(cheltuieli) == 3
    cheltuiala_modificata_1 = get_by_id(2, cheltuieli)
    assert get_suma(cheltuiala_modificata_1) == 410
    assert get_data(cheltuiala_modificata_1) == "04.06.2002"
    cheltuiala_modificata_2 = get_by_id(3, cheltuieli)
    assert get_suma(cheltuiala_modificata_2) == 108.5
    assert get_data(cheltuiala_modificata_2) == "04.06.2002"
    cheltuiala_nemodificata = get_by_id(1, cheltuieli)
    assert get_suma(cheltuiala_nemodificata) == 154.35
    assert get_data(cheltuiala_nemodificata) == "23.06.2021"

def test_ordonare_cheltuieli():
    pass
    """p1 = create_cheltuiala('id2', 1, 120.9, '04.06.2002', 'alte cheltuieli')
    p2 = create_cheltuiala('id2', 6, 98.4, '04.09.2002', 'alte cheltuieli')
    p3 = create_cheltuiala('id1', 7, 453.5, '04.03.2002', 'alte cheltuieli')

    sorted_list = sort_cheltuieli([p1,p2,p3])
    assert sorted_list[0] == p2
    assert sorted_list[1] == p1
    assert sorted_list[2] == p3"""

