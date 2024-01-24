import pytest

from src.keyboard import Keyboard


@pytest.fixture
def kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_change_lang(kb):
    assert kb.language == "EN"
    kb.change_lang()
    assert kb.language == "RU"
    kb.change_lang()
    assert kb.language == "EN"


def test_language(kb):
    assert kb.language == "EN"
    with pytest.raises(AttributeError):
        kb.language = "CH"
