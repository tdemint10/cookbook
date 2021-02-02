from pytest import fixture

from .model import Recipe


@fixture
def recipe() -> Recipe:
    return Recipe(name="test_recipe")


def test_recipe_create(recipe: Recipe):
    assert recipe
    assert recipe.name == "test_recipe"
