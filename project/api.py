from ninja_extra import api_controller, route
from .models import Project
from .schemas import ProjectSchema

@api_controller('/projects', tags=['Projects'], permissions=[])
class ProjectController:
    @route.get("/")
    def list(self, place_id: int = None):
        projects = Project.objects.all()
        if place_id is not None:
            projects = Project.objects.filter(place = place_id)
        result = [ProjectSchema.from_orm(p).dict() for p in projects]
        return result