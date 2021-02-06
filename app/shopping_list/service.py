import bson

from typing import List

from .model import ShoppingList
from .interface import ShoppingListInterface, ShoppingListItemInterface

from app.recipe.model import Recipe
from app.recipe.service import RecipeService


class ShoppingListService:

    @staticmethod
    def get_all() -> List[ShoppingList]:
        return ShoppingList.objects


    @staticmethod
    def get_by_id(id: str) -> ShoppingList:
        return ShoppingList.objects(id=bson.objectid.ObjectId(id)).first()


    @staticmethod
    def get_current() -> ShoppingList:
        return ShoppingList.objects(is_current=True).first()


    @staticmethod
    def add_recipe(shopping_list_id: str, recipe_id: str) -> ShoppingList:
        shopping_list: ShoppingList = ShoppingListService.get_by_id(shopping_list_id)
        recipe: Recipe = RecipeService.get_by_id(recipe_id)

        # create easy-to-parse json
        items_json = {}
        for item in shopping_list.items:
            items_json[item.name] = {"amount": item.amount, "unit": item.unit}

        # update the values
        for ingredient in recipe.ingredients:
            if ingredient.name in items_json:
                items_json[ingredient.name]["amount"] += ingredient.amount
            else:
                items_json[ingredient.name] = {"amount": ingredient.amount, "unit": ingredient.unit}

        # convert back to the correct format
        items = []
        for name in items_json:
            items.append(dict(
                name=name,
                amount=items_json[name]["amount"],
                unit=items_json[name]["unit"]
            ))

        # append recipe id
        recipes = shopping_list.recipes
        recipes.append(str(recipe.id))

        # persist
        shopping_list.update(**{
            "set__items": items,
            "set__recipes": recipes
        })

        return ShoppingListService.get_by_id(shopping_list.id)


    @staticmethod
    def remove_recipe(shopping_list_id: str, recipe_id: str) -> ShoppingList:
        shopping_list: ShoppingList = ShoppingListService.get_by_id(shopping_list_id)
        recipe: Recipe = RecipeService.get_by_id(recipe_id)

        # create easy-to-parse json
        items_json = {}
        for item in shopping_list.items:
            items_json[item.name] = {"amount": item.amount, "unit": item.unit}

        # update the values
        for ingredient in recipe.ingredients:
            if items_json[ingredient.name]["amount"] == ingredient.amount:
                items_json.pop(ingredient.name, None)
            else:
                items_json[ingredient.name]["amount"] -= ingredient.amount

        # convert back to correct format
        items = []
        for name in items_json:
            items.append(dict(
                name=name,
                amount=items_json[name]["amount"],
                unit=items_json[name]["unit"]
            ))

        # remove recipe id
        recipe_ids = shopping_list.recipes
        recipe_ids.remove(str(recipe.id))

        # persist
        shopping_list.update(**{
            "set__items": items,
            "set__recipes": recipe_ids
        })

        return ShoppingListService.get_by_id(shopping_list.id)



    @staticmethod
    def delete_by_id(id: str) -> List[int]:
        shopping_list: ShoppingList = ShoppingListService.get_by_id(id)

        if not shopping_list:
            return []

        shopping_list.delete()

        return [id]


    @staticmethod
    def create() -> ShoppingList:
        old_shopping_list: ShoppingList = ShoppingListService.get_current()

        # only one current list
        if old_shopping_list:
            old_shopping_list.update(**{
                "set__is_current": False
            })

        new_shopping_list = ShoppingList(items=[], is_current=True).save()

        return new_shopping_list
