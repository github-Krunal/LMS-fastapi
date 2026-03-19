from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str
    password: str
    name: str
    role: str = "student",
