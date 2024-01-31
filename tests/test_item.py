import pytest

from src.item import Item
from src.phone import Phone
from config import TEST_CSV, TEST_CSV_CRAZY
from src.exceptions import InstantiateCSVError


def test_init():
    """Тестирование инициализации"""
    item1 = Item("Смартфон", 10000, 20)
    item2 = Item("Ноутбук", 20000, 5)
    assert item1.name == "Смартфон"
    assert item1.price == 10000
    assert item1.quantity == 20
    assert Item.all == [item1, item2]


@pytest.fixture
def my_object():
    """Фикстура возвращает экземпляр"""
    return Item("Смартфон", 10000, 20)


def test_calculate_total_price(my_object):
    """Тестирование общей стоимости товара"""
    assert my_object.calculate_total_price() == 200000


def test_apply_discount(my_object):
    """Тестирование применения скидки"""
    my_object.pay_rate = 1.5
    my_object.apply_discount()
    assert my_object.price == 15000


def test_name_setter(my_object):
    my_object.name = 'Телефон'
    assert my_object.name == 'Телефон'
    # with pytest.raises(Exception):
    #     my_object.name = 'Супертелефон'
    my_object.name = 'Супертелефон'
    assert my_object.name == 'Супертелеф'


def test_instantiate_from_csv():
    Item.instantiate_from_csv(TEST_CSV)
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5


def test__repr_(my_object):
    assert repr(my_object) == "Item('Смартфон', 10000, 20)"


def test__str_(my_object):
    assert str(my_object) == 'Смартфон'


def test__add_(my_object):
    phone1 = Phone("iPhone 14", 120_000, 5, 2)
    assert my_object + phone1 == 25
    assert phone1 + phone1 == 10
    assert my_object + my_object == 40
    assert phone1 + my_object == 25
    with pytest.raises(ValueError, match="Складывать можно только экземпляры класса"):
        my_object + 5
        my_object + "Hello"


def test_instantiate_from_csv_not_found():
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv("test")
        Item.instantiate_from_csv("")


def test_instantiate_from_csv_key_error():
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv(TEST_CSV_CRAZY)