from ninja import NinjaAPI
from developer.api import router as developer_router
from project.api import router as project_router
from .AuthBearer import AuthBearer

api = NinjaAPI(title="xCity", description="Api docs for real estate project.", csrf=True)

api.add_router('/developers', developer_router)
api.add_router('/projects', project_router)

@api.get("/bearer", auth=AuthBearer())
def bearer(request):
    return {"token": request.auth}