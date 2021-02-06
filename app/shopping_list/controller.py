from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import ShoppingListSchema
from .service import ShoppingListService
from .model import ShoppingList
from .interface import ShoppingListInterface

api = Namespace("ShoppingList", description="Shopping List API")


@api.route("/")
class ShoppingListResource(Resource):
    """ Shopping List """

    @responds(schema=ShoppingListSchema(many=True))
    def get(self) -> List[ShoppingList]:
        """ Get all ShoppingList """

        shopping_lists = ShoppingListService.get_all()
        return shopping_lists


    @responds(schema=ShoppingListSchema)
    def post(self) -> ShoppingList:
        """ Create a Shopping List """

        return ShoppingListService.create()


@api.route("/<string:shoppingListId>")
@api.param("shoppingListId", "Shopping List ID")
class ShoppingListIdResource(Resource):

    @responds(schema=ShoppingListSchema)
    def get(self, shoppingListId: str) -> ShoppingList:
        """ Get single ShoppingList """

        return ShoppingListService.get_by_id(shoppingListId)


    def delete(self, shoppingListId: str) -> Response:
        """ Delete single ShoppingList """
        from flask import jsonify

        id = ShoppingListService.delete_by_id(shoppingListId)
        return jsonify(dict(status="Success", id=id))


@api.route("/current")
class ShoppinglistCurrentResource(Resource):

    @responds(schema=ShoppingListSchema)
    def get(self) -> ShoppingList:
        """ Get current Shopping List """

        return ShoppingListService.get_current()


@api.route("/<string:shoppingListId>/add/<string:recipeId>")
@api.param("shoppingListId", "Shopping List ID")
@api.param("recipeId", "Recipe ID")
class ShoppingListAddResource(Resource):

    @responds(schema=ShoppingListSchema)
    def put(self, shoppingListId: str, recipeId: str) -> ShoppingList:
        """ Add Recipe to ShoppingList """

        return ShoppingListService.add_recipe(shoppingListId, recipeId)


@api.route("/<string:shoppingListId>/remove/<string:recipeId>")
@api.param("shoppingListId", "Shopping List ID")
@api.param("recipeId", "Recipe ID")
class ShoppingListRemoveResource(Resource):

    @responds(schema=ShoppingListSchema)
    def put(self, shoppingListId: str, recipeId: str) -> ShoppingList:
        """ Remove Recipe from ShoppingList """

        return ShoppingListService.remove_recipe(shoppingListId, recipeId)
