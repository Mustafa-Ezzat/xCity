from ninja import File, UploadedFile, Form
from ninja_extra import api_controller, route
from ninja.security import django_auth
from .models import Developer
from .schemas import DeveloperSchemaIn, DeveloperSchemaOut

@api_controller("/developers", tags=['Developers'], permissions=[])
class DeveloperController:
    @route.get("/")
    def list(self):
        developers = Developer.objects.all() 
        return [DeveloperSchemaOut.from_orm(d) for d in developers]
    
    @route.post("/create")
    def create(self, payload: Form[DeveloperSchemaIn], file: File[UploadedFile]):
        obj = Developer()
        for key, val in payload.dict(exclude_unset=True).items():
            setattr(obj, key, val)
        obj.img_url = file
        obj.save()
        return {"message": f"The developer created successfully."}
    
    @route.post("/update", response={200: dict, 403: dict})
    def update(self, id: Form[int], payload: Form[DeveloperSchemaIn], file: File[UploadedFile]):
        try:
            obj = Developer.objects.get(id = id)
            for key, val in payload.dict(exclude_unset=True).items():
                setattr(obj, key, val)
            obj.img_url = file
            obj.save()
            return {"message": "The developer updated successfully."}
        except Developer.DoesNotExist:
            return 403, {"message": "The developer no longer available."}

    @route.delete("/delete/{id}", response={200: dict, 403: dict})
    def delete(self, id: int):
        try:
            obj = Developer.objects.get(id = id)
            obj.delete()
            return {"message": "The developer deleted successfully."}
        except Developer.DoesNotExist:
            return 403, {"message": "The developer no longer available."}
