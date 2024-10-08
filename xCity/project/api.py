from ninja import Router
from ninja.security import django_auth
from .models import Project
from .schemas import ProjectSchema

router = Router()

@router.get('/', auth=django_auth)
def list(request):
    projects = Project.objects.all()
    return [ProjectSchema.from_orm(p) for p in projects]