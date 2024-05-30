from pydantic import BaseModel


class AuthModel(BaseModel):
    user_id: str
    password: str
