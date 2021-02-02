from marshmallow import fields, Schema


class IngredientSchema(Schema):
    """ Ingredient Schema """

    name = fields.String(attribute="name")
    amount = fields.Number(attribute="amount")
    unit = fields.String(attribute="unit")

class RecipeSchema(Schema):
    """ Recipe Schema """

    id = fields.String(attribute="id")
    name = fields.String(attribute="name")
    description = fields.String(attribute="description")
    imageUrl = fields.String(attribute="image_url")
    isFavorite = fields.Boolean(attribute="is_favorite")
    ingredients = fields.List(fields.Nested(IngredientSchema))
    directions = fields.List(fields.String(), attribute="directions")
