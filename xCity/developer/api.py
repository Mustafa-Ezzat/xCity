from ninja import Router

router = Router()

@router.get('/{developer_name}')
def hello(request, developer_name: str):
    return f"Hello, {developer_name}"