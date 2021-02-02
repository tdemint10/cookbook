from flask import request
from flask_accepts import accepts, responds
from flask_restx import Namespace, Resource
from flask.wrappers import Response
from typing import List

from .schema import RecipeSchema
from .service import RecipeService
from .model import Recipe
from .interface import RecipeInterface

api = Namespace("Recipe", description="Recipe API")


@api.route("/")
class RecipeResource(Resource):
    """ Recipes """

    @responds(schema=RecipeSchema(many=True))
    def get(self) -> List[Recipe]:
        """ Get all Recipes """

        recipes = RecipeService.get_all()
        return recipes


    @accepts(schema=RecipeSchema, api=api)
    @responds(schema=RecipeSchema)
    def post(self) -> Recipe:
        """ Create a single Recipe """

        return RecipeService.create(request.parsed_obj)


@api.route("/<string:recipeId>")
@api.param("recipeId", "Recipe ID")
class RecipeIdResource(Resource):

    @responds(schema=RecipeSchema)
    def get(self, recipeId: str) -> Recipe:
        """ Get single Recipe """

        return RecipeService.get_by_id(recipeId)


    def delete(self, recipeId: str) -> Response:
        """ Delete singe Recipe """
        from flask import jsonify

        id = RecipeService.delete_by_id(recipeId)
        return jsonify(dict(status="Success", id=id))


    @accepts(schema=RecipeSchema, api=api)
    @responds(schema=RecipeSchema)
    def put(self, recipeId: str) -> Recipe:
        """ Update single Recipe """

        updates: RecipeInterface = request.parsed_obj
        recipe: Recipe = RecipeService.get_by_id(recipeId)

        return RecipeService.update(recipe, updates)


@api.route("/name/<string:recipeName>")
@api.param("recipeName", "Recipe Name")
class RecipeNameResource(Resource):

    @responds(schema=RecipeSchema(many=True))
    def get(self, recipeName: str) -> List[Recipe]:
        """ Get Recipes with name """

        return RecipeService.get_by_name(recipeName)
