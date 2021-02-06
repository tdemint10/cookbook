from pytest import fixture

from .model import ShoppingList
from .schema import ShoppingListSchema, ShoppingListItemSchema
from .interface import ShoppingListInterface


@fixture
def schema() -> ShoppingListSchema:
    return ShoppingListSchema()


def test_shopping_list_schema_create(schema: ShoppingListSchema):
    assert schema


def test_shopping_list_schema_works(schema: ShoppingListSchema):
    params: ShoppingListInterface = schema.load({"items": [{"name": "item_1", "amount": 1.0, "unit": "unit"}], "recipes": ["id_1", "id_2"], "isCurrent": True})
    shopping_list = ShoppingList(**params)

    assert shopping_list
    assert shopping_list.created_at
    assert len(shopping_list.items) == 1
    assert len(shopping_list.recipes) == 2

    item = shopping_list.items[0]

    assert item
    assert item.name == "item_1"
    assert item.amount == 1.0
    assert item.unit == "unit"

    assert shopping_list.is_current
