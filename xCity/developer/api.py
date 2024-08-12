from ninja import Router
from .models import Developer
from .schemas import DeveloperSchema

router = Router()

@router.get("/")
def list(request):
    developers = Developer.objects.all() 
    return [DeveloperSchema.from_orm(d) for d in developers]

@router.post("/create")
def create(request, payload: DeveloperSchema):
    obj = Developer()
    for key, val in payload.dict(exclude_unset=True).items():
        setattr(obj, key, val)
    obj.save()
    return {"message": "The developer created successfully."}

@router.patch("/update/{id}", response={200: dict, 403: dict})
def update(request, id: int, payload: DeveloperSchema):
    try:
        obj = Developer.objects.get(id = id)
        for key, val in payload.dict(exclude_unset=True).items():
            setattr(obj, key, val)
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
