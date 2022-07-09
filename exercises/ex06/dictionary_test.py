"""Testing the functions within in dictionary."""
__author__ = "730466380"

from exercises.ex06.dictionary import invert
from exercises.ex06.dictionary import favorite_color
from exercises.ex06.dictionary import count
import pytest


def test_invert_nothing() -> None:
    """Tests for nothing in the dict."""
    things: dict[str, str] = {}
    assert invert(things) == {}


def test_invert_one_item() -> None:
    """Asserts that with one pair, they switch spots."""
    things: dict[str, str] = {'kyra': 'pollock'}
    assert invert(things) == {'pollock': 'kyra'}


def test_invert_multiple_items() -> None:
    """Tests for when there are multiple of the same value."""
    things: dict[str, str] = {
        'pizza': 'party',
        'surprise': 'yay',
        'fun': 'pencil'
    }
    expected_inv: dict[str, str] = {
        'party': 'pizza',
        'yay': 'surprise',
        'pencil': 'fun'
    }
    assert invert(things) == expected_inv


def test_invert_error() -> None:
    """Tests to make sure the KeyError is being raised."""
    with pytest.raises(KeyError):
        things: dict[str, str] = {
            'pizza': 'party',
            'surprise': 'party'
        }
        invert(things)


def test_favorite_color_one() -> None:
    """Tests for output with one entry."""
    color_dict: dict[str, str] = {'kyra': 'green'}
    expected: str = 'green'
    assert favorite_color(color_dict) == expected


def test_favorite_color_tie() -> None:
    """Tests favorite color is starts with a letter higher in alphabet if tied with another."""
    color_dict: dict[str, str] = {
        'candace': 'green',
        'perry': 'blue',
        'ferb': 'blue',
        'phineas': 'green'
    }
    expected: str = 'green'
    assert favorite_color(color_dict) == expected


def test_favorite_tied() -> None:
    """Tests the output when there is one of each color."""
    color_dict: dict[str, str] = {
        'perry': 'pink',
        'ferb': 'blue',
        'candace': 'black',
        'phineas': 'green'
    }
    expected: str = 'pink'
    assert favorite_color(color_dict) == expected


def test_count_nothing() -> None:
    """Testing for an empty list."""
    num_list: list[str] = {}
    expected_frequency: dict[str, str] = {}
    assert count(num_list) == expected_frequency


def test_count_same() -> None:
    """Testing output if there are the two different words are in the list the same amount."""
    num_list: list[str] = ["pizza", "ranch", "tired", "pizza", "ranch"]
    expected_output: dict[str, int] = {
        "pizza": 2,
        "ranch": 2,
        "tired": 1
    }
    assert count(num_list) == expected_output


def test_count_normal() -> None:
    """Testing a list with normal values."""
    num_list: list[str] = ["time", "time", "time", "count", "count", "tired"]
    expected_output: dict[str, int] = {
        "time": 3,
        "count": 2,
        "tired": 1
    }
    assert count(num_list) == expected_output