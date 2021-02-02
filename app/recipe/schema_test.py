from pytest import fixture

from .model import Recipe
from .schema import RecipeSchema
from .interface import RecipeInterface


@fixture
def schema() -> RecipeSchema:
    return RecipeSchema()


def test_recipe_schema_create(schema: RecipeSchema):
    assert schema


def test_recipe_schema_works(schema: RecipeSchema):
    params: RecipeInterface = schema.load({"name": "recipe_test"})
    recipe = Recipe(**params)

    assert recipe.name == "recipe_test"
