import pytest
from Funciones import add_digits, fill_word

def test_sum_digits():
    assert add_digits(123)==6

@pytest.mark.parametrize(
        "input_number, expected",
        [
            (458, 17),
            (920, 11),
            (add_digits(5261), 5),
            (8375, 23),
            (add_digits(62934), 6)
        ]
)
def test_sum_digits_parameters(input_number,expected):
    assert add_digits(input_number)==expected


def test_fill_word():
    assert fill_word("UAI", "USUARIO")=="U_UA_I_"

@pytest.mark.parametrize(
        "input_characters, input_hidden_word, expected",
        [
            ("AODRH", "ARCHIVO", "AR_H__O"),
            ("NTE", "INTERNET", "_NTE_NET"),
            ("MPSR", "IMPRESORA", "_MPR_S_R_"),            
        ]
)
def test_fill_word_parameters(input_characters, input_hidden_word, expected):
    assert fill_word(input_characters, input_hidden_word)==expected

