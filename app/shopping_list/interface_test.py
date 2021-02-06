from pytest import fixture

from .model import ShoppingList
from .interface import ShoppingListInterface, ShoppingListItemInterface


@fixture
def interface() -> ShoppingListInterface:
    return ShoppingListInterface(items=[ShoppingListItemInterface(name="item_1", amount=1.0, unit="unit")], recipes=["id_1", "id_2"], is_current=False)


def test_shopping_list_interface_create(interface: ShoppingListInterface):
    assert interface


def test_shopping_list_interface_works(interface: ShoppingListInterface):
    shopping_list = ShoppingList(**interface)
    assert shopping_list
