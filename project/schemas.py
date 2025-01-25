from ninja import ModelSchema
from .models import Project

class ProjectSchema(ModelSchema):
    class Meta:
        model = Project
        fields = [
            "id", 
            "name", 
            "starting_price", 
            "delivery", 
            "payment_plan", 
            "reward", 
            "img_url",
            "developer", 
            "place"
        ]