from .model import ShoppingList
from .schema import ShoppingListSchema

BASE_ROUTE = "shoppingList"


def register_routes(api, app, root="api"):
    from .controller import api as shopping_list_api

    api.add_namespace(shopping_list_api, path=f"/{root}/{BASE_ROUTE}")
