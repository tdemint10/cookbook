from marshmallow import fields, Schema


class ShoppingListItemSchema(Schema):
    """ ShoppingListItem Schema """

    name = fields.String(attribute="name")
    amount = fields.Number(attribute="amount")
    unit = fields.String(attribute="unit")


class ShoppingListSchema(Schema):
    """ ShoppingList Schema """

    id = fields.String(attribute="id")
    createdAt = fields.String(attribute="created_at")
    items = fields.List(fields.Nested(ShoppingListItemSchema))


class RecipeIdsSchema(Schema):
    """ RecipeIds Schema """

    ids = fields.List(fields.String(), attribute="ids")
