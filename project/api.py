from ninja_extra import api_controller, route
from .models import Project
from .schemas import ProjectSchema

@api_controller('/projects', tags=['Projects'], permissions=[])
class ProjectController:
    @route.get("/")
    def list(self):
        projects = Project.objects.all()
        return [ProjectSchema.from_orm(p).dict() for p in projects]