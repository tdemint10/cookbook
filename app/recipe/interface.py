from mypy_extensions import TypedDict
from typing import List


class IngredientInterface(TypedDict, total=False):
    name: str
    amount: float
    unit: str


class RecipeInterface(TypedDict, total=False):
    name: str
    created_at: str
    description: str
    is_favorite: bool
    image_url: str
    ingredients: List[IngredientInterface]
    directions: List[str]
