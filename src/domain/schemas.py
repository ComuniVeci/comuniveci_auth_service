from pydantic import BaseModel, EmailStr, Field

class UserCreateSchema(BaseModel):
    email: EmailStr
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6)

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str
