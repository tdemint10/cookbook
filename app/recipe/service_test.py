import mongoengine

from typing import List

from app.test.fixtures import app, db

from .model import Recipe
from .service import RecipeService
from .interface import IngredientInterface, RecipeInterface


def test_get_all(db: mongoengine):
    recipe_1: Recipe = Recipe(name="test_recipe_1")
    recipe_2: Recipe = Recipe(name="test_recipe_2")

    recipe_1.save()
    recipe_2.save()

    results: List[Recipe] = RecipeService.get_all()

    assert len(results) == 2
    assert recipe_1 in results and recipe_2 in results


def test_get_by_id(db: mongoengine):
    recipe_1: Recipe = Recipe(name="test_recipe_1")
    recipe_2: Recipe = Recipe(name="test_recipe_2")

    recipe_1.save()
    recipe_2.save()

    result: Recipe = RecipeService.get_by_id(recipe_1.id)

    assert result == recipe_1


def test_get_by_name(db: mongoengine):
    recipe_1: Recipe = Recipe(name="test_recipe_1")
    recipe_2: Recipe = Recipe(name="test_recipe_2")

    recipe_1.save()
    recipe_2.save()

    results: List[Recipe] = RecipeService.get_by_name("test_recipe_1")

    assert len(results) == 1
    assert recipe_1 in results


def test_update(db: mongoengine):
    recipe: Recipe = Recipe(name="test_recipe", ingredients=[])

    recipe.save()

    ingredient = IngredientInterface(name="item_1", amount=1.0, unit="cup")
    result: Recipe = RecipeService.update(recipe, RecipeInterface(ingredients=[ingredient]))

    assert result["name"] == "test_recipe"
    assert len(result["ingredients"]) == 1


def test_delete(db: mongoengine):
    recipe: Recipe = Recipe(name="test_recipe")

    recipe.save()

    result: List[int] = RecipeService.delete_by_id(recipe["id"])

    assert len(Recipe.objects) == 0


def test_create(db: mongoengine):
    recipe: RecipeInterface = dict(name="test_recipe", ingredients=[])

    create_result: Recipe = RecipeService.create(recipe)

    assert create_result

    query_result: List[Recipe] = Recipe.objects

    assert len(query_result) == 1

    for key in recipe.keys():
        assert getattr(query_result[0], key) == recipe[key]
