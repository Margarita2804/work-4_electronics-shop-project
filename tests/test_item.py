import pytest

from src.item import Item


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
