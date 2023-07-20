import pytest
from utils import str_to_bool


# def test_yes_is_true():
#     result = str_to_bool('yes')
#     assert result is True


# def test_y_is_true():
#     result = str_to_bool('y')
#     assert result is True


# def test_no_is_false():
#     result = str_to_bool('no')
#     assert result is False


# def test_n_is_false():
#     result = str_to_bool('n')
#     assert result is False


@pytest.mark.parametrize('value', ['y', 'yes', ''])
def test_is_true(value):
    result = str_to_bool(val=value)
    assert result is True


@pytest.mark.parametrize('value', ['nl', 'no'])
def test_is_false(value):
    result = str_to_bool(val=value)
    assert result is False
