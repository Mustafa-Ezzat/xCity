from ninja import ModelSchema
from .models import Developer

class DeveloperSchema(ModelSchema):
    class Meta:
        model = Developer
        fields = ["name"]