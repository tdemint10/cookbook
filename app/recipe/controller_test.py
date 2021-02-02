from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app
from .service import RecipeService
from .schema import RecipeSchema
from .model import Recipe
from .interface import RecipeInterface
from . import BASE_ROUTE


def make_recipe(
        id="123", name = "recipe", ingredients = []
    ) -> Recipe:
        recipe = Recipe(id=id, name=name, ingredients=ingredients)
        return recipe


class TestRecipeResource:

    @patch.object(
        RecipeService,
        "get_all",
        lambda: [
            make_recipe(name="test_recipe_1"),
            make_recipe(name="test_recipe_2"),
        ],
    )
    def test_get_all(self, client: FlaskClient):
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()
            expected = (
                RecipeSchema(many=True)
                .dump(
                    [
                        make_recipe(name="test_recipe_1"),
                        make_recipe(name="test_recipe_2"),
                    ]
                )
            )

            for r in results:
                assert r in expected

    @patch.object(
        RecipeService, "create", lambda create_request: Recipe(**create_request)
    )
    def test_post(self, client: FlaskClient):
        with client:
            payload = dict(name="test_recipe", ingredients=[])
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = (
                RecipeSchema()
                .dump(Recipe(name=payload["name"], ingredients=payload["ingredients"]))
            )

            assert result == expected


def fake_update(recipe: Recipe, updates: RecipeInterface) -> Recipe:
    return Recipe(id="123", name=updates["name"], ingredients=updates["ingredients"])


class TestRecipeIdResource:

    @patch.object(RecipeService, "get_by_id", lambda id: make_recipe(id=id, name="test_recipe"))
    def test_get(self, client: FlaskClient):
        with client:
            result: Recipe = client.get(f"/api/{BASE_ROUTE}/123").get_json()
            expected: Recipe = make_recipe(id="123", name="test_recipe")

            assert result["name"] == expected.name


    @patch.object(RecipeService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):
        with client:
            result = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id="123")

            assert result == expected


    @patch.object(RecipeService, "get_by_id", lambda id: make_recipe(id=id))
    @patch.object(RecipeService, "update", fake_update)
    def test_put(self, client: FlaskClient):
        with client:
            result = client.put(
                f"/api/{BASE_ROUTE}/123",
                json={"name": "updated_name", "ingredients": []}
            ).get_json()

            expected = (
                RecipeSchema()
                .dump(Recipe(id="123", name="updated_name", ingredients=[]))
            )

            assert result == expected


class TestRecipeNameResource:

    @patch.object(RecipeService, "get_by_name", lambda name: [make_recipe(name="test_recipe")])
    def test_get(self, client: FlaskClient):
        with client:
            result = client.get(f"/api/{BASE_ROUTE}/name/test_recipe").get_json()
            expected = make_recipe(name="test_recipe")

            assert result[0]["name"] == expected.name
