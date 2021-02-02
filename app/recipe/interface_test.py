from pytest import fixture

from .model import Recipe
from .interface import RecipeInterface


@fixture
def interface() -> RecipeInterface:
    return RecipeInterface(name="recipe_test")


def test_recipe_interface_create(interface: RecipeInterface):
    assert interface


def test_recipe_interface_works(interface: RecipeInterface):
    recipe = Recipe(**interface)
    assert recipe
