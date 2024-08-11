from ninja import NinjaAPI
from developer.api import router as developer_router
from project.api import router as project_router

api = NinjaAPI()

api.add_router('/developer', developer_router)
api.add_router('project', project_router)