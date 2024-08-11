from ninja import Router

router = Router()

@router.get('/{project_name}')
def hello(request, project_name: str):
    return f"Hello, {project_name}"