import datetime
import mongoengine


class ShoppingListItem(mongoengine.EmbeddedDocument):
    """ ShoppingListItem Model """

    name = mongoengine.StringField(required=True)
    amount = mongoengine.DecimalField()
    unit = mongoengine.StringField()


class ShoppingList(mongoengine.Document):
    """ ShoppingList Model """

    created_at = mongoengine.DateTimeField(required=True, default=datetime.datetime.utcnow)
    items = mongoengine.ListField(mongoengine.EmbeddedDocumentField(ShoppingListItem))
