from ninja import ModelSchema
from .models import Place

class PlaceSchemaIn(ModelSchema):
    class Meta:
        model = Place
        fields = ["name"]

class PlaceSchemaOut(ModelSchema):
    class Meta:
        model = Place
        fields = ["id", "name"]