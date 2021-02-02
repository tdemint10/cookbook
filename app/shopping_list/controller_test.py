from unittest.mock import patch
from flask.testing import FlaskClient

from app.test.fixtures import client, app
from .service import ShoppingListService
from .schema import ShoppingListSchema, RecipeIdsSchema
from .model import ShoppingList
from .interface import ShoppingListInterface, RecipeIdsInterface
from . import BASE_ROUTE


def make_shopping_list(items=[]) -> ShoppingList:
    shopping_list = ShoppingList(items=items)
    return shopping_list


class TestShoppingListResource:

    @patch.object(
        ShoppingListService,
        "get_all",
        lambda: [
            make_shopping_list(),
            make_shopping_list(),
        ]
    )
    def test_get_all(self, client: FlaskClient):
        with client:
            results = client.get(f"/api/{BASE_ROUTE}", follow_redirects=True).get_json()

            assert len(results) == 2


    @patch.object(
        ShoppingListService, "create", lambda: make_shopping_list()
    )
    def test_post(self, client: FlaskClient):
        with client:
            payload = dict(ids=["id_1", "id_2"])
            result = client.post(f"/api/{BASE_ROUTE}/", json=payload).get_json()
            expected = make_shopping_list()

            assert len(result["items"]) == len(expected.items)


class TestShoppingListIdResource:

    @patch.object(ShoppingListService, "get_by_id", lambda id: make_shopping_list())
    def test_get(self, client: FlaskClient):
        with client:
            result: ShoppingList = client.get(f"/api/{BASE_ROUTE}/123").get_json()

            assert result


    @patch.object(ShoppingListService, "delete_by_id", lambda id: id)
    def test_delete(self, client: FlaskClient):
        with client:
            result: ShoppingList = client.delete(f"/api/{BASE_ROUTE}/123").get_json()
            expected = dict(status="Success", id="123")

            assert result == expected


class TestShoppingListAddResource:

    @patch.object(ShoppingListService, "add_recipe", lambda id_1, id_2: make_shopping_list())
    def test_put(self, client: FlaskClient):
        with client:
            result: ShoppingList = client.put(f"/api/{BASE_ROUTE}/123/add/456").get_json()

            assert result


class TestShoppingListRemoveResource:

    @patch.object(ShoppingListService, "remove_recipe", lambda id_1, id_2: make_shopping_list())
    def test_put(self, client: FlaskClient):
        with client:
            result: ShoppingList = client.put(f"/api/{BASE_ROUTE}/123/remove/456").get_json()

            assert result
