from ninja import NinjaAPI, Schema, Path, File, Form
from ninja.files import UploadedFile
from typing import List

api = NinjaAPI()

class Location(Schema):
    country: str
    city: str
    zip_code: str

    def value(self):
        return f"Location: {self.country}, {self.city}, {self.zip_code}"

class User(Schema):
    username: str = None
    email: str = None
    first_name: str = None
    last_name: str = None

class Error(Schema):
    message: str

@api.get("/locations")
def locations(request):
    return {"locations": []}

@api.get("/projects")
def projects(request):
    return {"projects": []}

@api.post("/location")
def location(request, data: Location):
    return f"Hello, {data.name}"

@api.get("/me", response = {200: User, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first."}
    return request.user

@api.get("locations/{country}/{city}/{zip_code}")
def locations(request, location: Path[Location]):
    return location.value()

@api.post("/upload")
def upload(request, file: File[UploadedFile]):
    data = file.read()
    return {"name": file.name, "len": len(data)}

@api.post("/upload_many")
def upload_many(request, files: File[List[UploadedFile]]):
    return [ {"name": f.name} for f in files]

@api.post("/create_user")
def create_user(request, details: Form[User], file: File[UploadedFile]):
    return {"user": details.dict(), "file_name": file.name}

@api.post('/users')
def create_user(request, details: Form[User], files: File[list[UploadedFile]]):
    return [details.dict(), [f.name for f in files]]