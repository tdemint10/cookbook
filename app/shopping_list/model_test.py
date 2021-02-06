from pytest import fixture

from .model import ShoppingList, ShoppingListItem


@fixture
def shopping_list() -> ShoppingList:
    return ShoppingList(items=[ShoppingListItem(name="item_1", amount=1.0, unit="unit")], recipes=["id_1", "id_2"], is_current=False)


def test_shopping_list_create(shopping_list: ShoppingList):
    assert shopping_list
    assert shopping_list.created_at
    assert len(shopping_list.items) == 1
    assert len(shopping_list.recipes) == 2

    item = shopping_list.items[0]

    assert item
    assert item.name == "item_1"
    assert item.amount == 1.0
    assert item.unit == "unit"

    assert not shopping_list.is_current
