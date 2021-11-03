from Logic.crud import add_cheltuiala
from Logic.operatiuni import stergere_toate_cheltuieli, sort_cheltuieli
from Domain.cheltuiala import create_cheltuiala


def test_stergere_toate_cheltuieli():
    cheltuieli = []
    cheltuieli = add_cheltuiala(cheltuieli, 'id1', 1, 120.9, '04.06.2002', 'alte cheltuieli')
    cheltuieli = add_cheltuiala(cheltuieli, 'id2', 4, 120.9, '04.07.2002', 'alte cheltuieli')
    cheltuieli = add_cheltuiala(cheltuieli, 'id3', 4, 145.8, '04.07.2002', 'alte cheltuieli')
    assert len(cheltuieli) == 3
    cheltuieli = stergere_toate_cheltuieli(cheltuieli, 4)
    assert len(cheltuieli) == 1

def test_ordonare_cheltuieli():
    pass
    #p1 = create_cheltuiala('id2', 1, 120.9, '04.06.2002', 'alte cheltuieli')
    #p2 = create_cheltuiala('id2', 6, 120.9, '04.09.2002', 'alte cheltuieli')
    #p3 = create_cheltuiala('id1', 7, 120.9, '04.03.2002', 'alte cheltuieli')

    #sorted_list = sort_cheltuieli([p1,p2,p3])
    #assert sorted_list[0] == p3
    #assert sorted_list[1] == p2
    #assert sorted_list[2] == p1

