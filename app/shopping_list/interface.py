from mypy_extensions import TypedDict
from typing import List


class ShoppingListItemInterface(TypedDict, total=False):
    name: str
    amount: float
    unit: str


class ShoppingListInterface(TypedDict, total=False):
    created_at: str
    items: List[ShoppingListItemInterface]
    recipes: List[str]
    is_current: bool
