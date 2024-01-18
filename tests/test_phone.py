import pytest

from src.phone import Phone


@pytest.fixture
def phone():
    return Phone("iPhone 15", 140_000, 5, 2)


def test_init(phone):
    assert phone.name == "iPhone 15"
    assert phone.price == 140000
    assert phone.quantity == 5
    assert phone.number_of_sim == 2


def test__repr_(phone):
    assert repr(phone) == "Phone('iPhone 15', 140000, 5, 2)"


def test__str_(phone):
    assert str(phone) == 'iPhone 15'


def test_getter(phone):
    assert phone.number_of_sim == 2


def test_setter(phone):
    phone.number_of_sim = 1
    assert phone.number_of_sim == 1
    with pytest.raises(ValueError, match="Количество физических SIM-карт должно быть целым числом больше нуля."):
        phone.number_of_sim = 0
        phone.number_of_sim = -1
        phone.number_of_sim = 0.5
