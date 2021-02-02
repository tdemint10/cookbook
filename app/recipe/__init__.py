from .model import Recipe
from .schema import RecipeSchema

BASE_ROUTE = "recipe"


def register_routes(api, app, root="api"):
    from .controller import api as recipe_api

    api.add_namespace(recipe_api, path=f"/{root}/{BASE_ROUTE}")
