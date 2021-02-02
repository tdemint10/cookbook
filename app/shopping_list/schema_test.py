from pytest import fixture

from .model import ShoppingList
from .schema import ShoppingListSchema, ShoppingListItemSchema, RecipeIdsSchema
from .interface import ShoppingListInterface, RecipeIdsInterface


@fixture
def schema() -> ShoppingListSchema:
    return ShoppingListSchema()


@fixture
def recipe_ids_schema() -> RecipeIdsSchema:
    return RecipeIdsSchema()


def test_shopping_list_schema_create(schema: ShoppingListSchema):
    assert schema


def test_shopping_list_schema_works(schema: ShoppingListSchema):
    params: ShoppingListInterface = schema.load({"items": [{"name": "item_1", "amount": 1.0, "unit": "unit"}]})
    shopping_list = ShoppingList(**params)

    assert shopping_list
    assert shopping_list.created_at
    assert len(shopping_list.items) == 1

    item = shopping_list.items[0]

    assert item
    assert item.name == "item_1"
    assert item.amount == 1.0
    assert item.unit == "unit"


def test_recipe_ids_schema_create(recipe_ids_schema: RecipeIdsSchema):
    assert recipe_ids_schema


def test_recipe_ids_schema_works(recipe_ids_schema: RecipeIdsSchema):
    params: RecipeIdsInterface = recipe_ids_schema.load({"ids": ["id_1", "id_2"]})

    assert params
