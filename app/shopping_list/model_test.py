from pytest import fixture

from .model import ShoppingList, ShoppingListItem


@fixture
def shopping_list() -> ShoppingList:
    return ShoppingList(items=[ShoppingListItem(name="item_1", amount=1.0, unit="unit")])


def test_shopping_list_create(shopping_list: ShoppingList):
    assert shopping_list
    assert shopping_list.created_at
    assert len(shopping_list.items) == 1

    item = shopping_list.items[0]

    assert item
    assert item.name == "item_1"
    assert item.amount == 1.0
    assert item.unit == "unit"
