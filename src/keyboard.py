from src.item import Item


class MixinKeyboard:
    """Класс Миксин"""
    def __init__(self, language="EN"):
        self.__language = language

    @property
    def language(self):
        """Геттер возвращающий язык"""
        return self.__language

    def change_lang(self):
        """Метод изменяющий язык"""
        if self.__language == "EN":
            self.__language = "RU"
        else:
            self.__language = "EN"


class Keyboard(Item, MixinKeyboard):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)
