import bson

from typing import List

from .model import Recipe
from .interface import RecipeInterface


class RecipeService:
    @staticmethod
    def get_all() -> List[Recipe]:
        return Recipe.objects


    @staticmethod
    def get_by_id(id: str) -> Recipe:
        return Recipe.objects(id=bson.objectid.ObjectId(id)).first()


    @staticmethod
    def get_by_name(name: str) -> Recipe:
        return Recipe.objects(name=name.strip())


    @staticmethod
    def update(recipe: Recipe, recipe_updates: RecipeInterface) -> Recipe:
        recipe.update(**{
                "set__name": recipe_updates["name"] if "name" in recipe_updates else recipe["name"],
                "set__description": recipe_updates["description"] if "description" in recipe_updates else recipe["description"],
                "set__image_url": recipe_updates["image_url"] if "image_url" in recipe_updates else recipe["image_url"],
                "set__is_favorite": recipe_updates["is_favorite"] if "is_favorite" in recipe_updates else recipe["is_favorite"],
                "set__ingredients": recipe_updates["ingredients"] if "ingredients" in recipe_updates else recipe["ingredients"],
                "set__directions": recipe_updates["directions"] if "directions" in recipe_updates else recipe["directions"],
            })

        return RecipeService.get_by_id(recipe.id)


    @staticmethod
    def delete_by_id(id: str) -> List[int]:
        recipe: Recipe = RecipeService.get_by_id(id)

        if not recipe:
            return []

        recipe.delete()

        return [id]


    @staticmethod
    def create(attrs: RecipeInterface) -> Recipe:
        new_recipe = Recipe(
            name=attrs["name"],
            description=attrs["description"] if "description" in attrs else "",
            image_url=attrs["image_url"] if "image_url" in attrs else "",
            is_favorite=attrs["is_favorite"] if "is_favorite" in attrs else False,
            ingredients=attrs["ingredients"] if "ingredients" in attrs else [],
            directions=attrs["directions"] if "directions" in attrs else []
        ).save()

        return new_recipe
