from pytest import fixture

from .model import ShoppingList
from .interface import ShoppingListInterface, ShoppingListItemInterface, RecipeIdsInterface


@fixture
def interface() -> ShoppingListInterface:
    return ShoppingListInterface(items=[ShoppingListItemInterface(name="item_1", amount=1.0, unit="unit")])


@fixture
def recipe_ids_interface() -> RecipeIdsInterface:
    return RecipeIdsInterface(ids=["id_1", "id_2"])


def test_shopping_list_interface_create(interface: ShoppingListInterface):
    assert interface


def test_shopping_list_interface_works(interface: ShoppingListInterface):
    shopping_list = ShoppingList(**interface)
    assert shopping_list


def test_recipe_ids_interface_create(recipe_ids_interface: RecipeIdsInterface):
    assert(recipe_ids_interface)
