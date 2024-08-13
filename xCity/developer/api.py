from ninja import Router, File, UploadedFile, Form
from .models import Developer
from .schemas import DeveloperSchemaIn, DeveloperSchemaOut

router = Router()

@router.get("/")
def list(request):
    developers = Developer.objects.all() 
    return [DeveloperSchemaOut.from_orm(d) for d in developers]

@router.post("/create")
def create(request, payload: Form[DeveloperSchemaIn], file: File[UploadedFile]):
    obj = Developer.objects.create(file)
    for key, val in payload.dict(exclude_unset=True).items():
        setattr(obj, key, val)
    obj.save()
    return {"message": f"The developer created successfully."}

@router.post("/update", response={200: dict, 403: dict})
def update(request, id: Form[int], payload: Form[DeveloperSchemaIn], file: File[UploadedFile]):
    try:
        obj = Developer.objects.get(id = id)
        for key, val in payload.dict(exclude_unset=True).items():
            setattr(obj, key, val)
        obj.img_url = file
        obj.save()
        return {"message": "The developer updated successfully."}
    except Developer.DoesNotExist:
        return 403, {"message": "The developer no longer available."}

@router.delete("/delete/{id}", response={200: dict, 403: dict})
def delete(request, id: int):
    try:
        obj = Developer.objects.get(id = id)
        obj.delete()
        return {"message": "The developer deleted successfully."}
    except Developer.DoesNotExist:
        return 403, {"message": "The developer no longer available."}
