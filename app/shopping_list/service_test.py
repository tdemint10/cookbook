import mongoengine

from typing import List

from app.test.fixtures import app, db
from app.recipe.model import Recipe, Ingredient

from .model import ShoppingList
from .service import ShoppingListService
from .interface import ShoppingListInterface, ShoppingListItemInterface, RecipeIdsInterface


def test_get_all(db: mongoengine):
    shopping_list_1: ShoppingList = ShoppingList(items=[])
    shopping_list_2: ShoppingList = ShoppingList(items=[])

    shopping_list_1.save()
    shopping_list_2.save()

    results: List[ShoppingList] = ShoppingListService.get_all()

    assert len(results) == 2
    assert shopping_list_1 in results and shopping_list_2 in results


def test_get_by_id(db: mongoengine):
    shopping_list_1: ShoppingList = ShoppingList(items=[])
    shopping_list_2: ShoppingList = ShoppingList(items=[])

    shopping_list_1.save()
    shopping_list_2.save()

    result: ShoppingList = ShoppingListService.get_by_id(shopping_list_1.id)

    assert result == shopping_list_1


def test_add_recipe(db: mongoengine):
    shopping_list: ShoppingList = ShoppingList(items=[])

    shopping_list.save()

    ingredient_1 = Ingredient(name="item_1", amount=1.0, unit="cup")
    recipe_1: Recipe = Recipe(name="test_recipe", ingredients=[ingredient_1])

    recipe_1.save()

    result_1: ShoppingList = ShoppingListService.add_recipe(shopping_list.id, recipe_1.id)

    assert len(result_1.items) == 1
    assert result_1.items[0].name == "item_1"
    assert result_1.items[0].amount == 1.0

    ingredient_2 = Ingredient(name="item_2", amount=3.0, unit="cup")
    recipe_2: Recipe = Recipe(name="test_recipe_2", ingredients=[ingredient_1, ingredient_2])

    recipe_2.save()

    result_2: ShoppingList = ShoppingListService.add_recipe(shopping_list.id, recipe_2.id)

    assert len(result_2.items) == 2
    assert result_2.items[0].name == "item_1"
    assert result_2.items[0].amount == 2.0
    assert result_2.items[1].name == "item_2"
    assert result_2.items[1].amount == 3.0


def test_remove_recipe(db: mongoengine):
    shopping_list: ShoppingList = ShoppingList(items=[])

    shopping_list.save()

    ingredient_1 = Ingredient(name="item_1", amount=1.0, unit="cup")
    recipe_1: Recipe = Recipe(name="test_recipe", ingredients=[ingredient_1])

    ingredient_2 = Ingredient(name="item_2", amount=3.0, unit="cup")
    recipe_2: Recipe = Recipe(name="test_recipe_2", ingredients=[ingredient_1, ingredient_2])

    recipe_1.save()
    recipe_2.save()

    ShoppingListService.add_recipe(shopping_list.id, recipe_1.id)
    ShoppingListService.add_recipe(shopping_list.id, recipe_2.id)

    result_1: ShoppingList = ShoppingListService.remove_recipe(shopping_list.id, recipe_2.id)

    assert len(result_1.items) == 1
    assert result_1.items[0].name == "item_1"
    assert result_1.items[0].amount == 1.0


def test_delete(db: mongoengine):
    shopping_list: ShoppingList = ShoppingList(items=[])

    shopping_list.save()

    result: List[int] = ShoppingListService.delete_by_id(shopping_list["id"])

    assert len(ShoppingList.objects) == 0


def test_create(db: mongoengine):
    create_result: ShoppingList = ShoppingListService.create()

    assert create_result

    query_result: List[ShoppingList] = ShoppingList.objects

    assert len(query_result) == 1
