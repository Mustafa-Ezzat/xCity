from ninja import ModelSchema
from .models import Developer

class DeveloperSchemaIn(ModelSchema):
    class Meta:
        model = Developer
        fields = ["name"]

class DeveloperSchemaOut(ModelSchema):
    class Meta:
        model = Developer
        fields = ["id", "name", "img_url"]