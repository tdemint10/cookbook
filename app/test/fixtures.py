import mongoengine

from pytest import fixture
from app import create_app
from app.recipe.model import Recipe
from app.shopping_list.model import ShoppingList


@fixture
def app():
    return create_app("test")


@fixture
def client(app):
    return app.test_client()


@fixture
def db(app):
    with app.app_context():
        Recipe.drop_collection()
        ShoppingList.drop_collection()
        yield db
        Recipe.drop_collection()
        ShoppingList.drop_collection()
