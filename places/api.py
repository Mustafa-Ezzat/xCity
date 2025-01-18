from ninja import Form
from ninja_extra import api_controller, route
from ninja.security import django_auth
from .models import Place
from .schemas import PlaceSchemaIn, PlaceSchemaOut

@api_controller("/places", tags=['Places'], permissions=[])
class PlaceController:
    @route.get("/")
    def list(self):
        developers = Place.objects.all() 
        return [PlaceSchemaOut.from_orm(d) for d in developers]
    
    @route.post("/create")
    def create(self, payload: Form[PlaceSchemaIn]):
        obj = Place()
        for key, val in payload.dict(exclude_unset=True).items():
            setattr(obj, key, val)
        obj.save()
        return {"message": f"The place created successfully."}
    
    @route.post("/update", response={200: dict, 403: dict})
    def update(self, id: int, payload: Form[PlaceSchemaIn]):
        try:
            obj = Place.objects.get(id = id)
            for key, val in payload.dict(exclude_unset=True).items():
                setattr(obj, key, val)
            obj.save()
            return {"message": "The place updated successfully."}
        except Place.DoesNotExist:
            return 403, {"message": "The place no longer available."}

    @route.delete("/delete/{id}", response={200: dict, 403: dict})
    def delete(self, id: int):
        try:
            obj = Place.objects.get(id = id)
            obj.delete()
            return {"message": "The place deleted successfully."}
        except Place.DoesNotExist:
            return 403, {"message": "The place no longer available."}
