from Tests.domain_test import cheltuiala_test
from Tests.test_crud import test_add_cheltuiala, test_edit_cheltuiala, test_delete_cheltuiala


def run_all_tests():
    test_add_cheltuiala()
    test_edit_cheltuiala()
    test_delete_cheltuiala()
    cheltuiala_test()