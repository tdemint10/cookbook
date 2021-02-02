import datetime
import mongoengine


class Ingredient(mongoengine.EmbeddedDocument):
    """ Ingredient Model """

    name = mongoengine.StringField(required=True)
    amount = mongoengine.DecimalField()
    unit = mongoengine.StringField()


class Recipe(mongoengine.Document):
    """ Recipe Model """

    name = mongoengine.StringField(required=True)
    created_at = mongoengine.DateTimeField(required=True, default=datetime.datetime.utcnow)
    description = mongoengine.StringField()
    image_url = mongoengine.StringField()
    is_favorite = mongoengine.BooleanField()
    ingredients = mongoengine.ListField(mongoengine.EmbeddedDocumentField(Ingredient))
    directions = mongoengine.ListField(mongoengine.StringField())
