from ninja import Router
from .models import Project
from .schemas import ProjectSchema

router = Router()

@router.get('/')
def list(request):
    projects = Project.objects.all()
    return [ProjectSchema.from_orm(p) for p in projects]