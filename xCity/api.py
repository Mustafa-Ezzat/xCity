from ninja_extra import NinjaExtraAPI
from developer.api import DeveloperController
from project.api import ProjectController
from places.api import PlaceController

api = NinjaExtraAPI(title="xCity", description="Api docs for real estate project.", csrf=True)

api.register_controllers(
    PlaceController,
    DeveloperController,
    ProjectController,
)