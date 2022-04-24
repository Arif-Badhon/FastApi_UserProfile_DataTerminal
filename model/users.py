from typing import Optional

from pydantic import BaseModel, EmailStr, Field

class UserModel(BaseModel):
    fullname: str = Field(...)
    email: EmailStr = Field(...)
    designation: str = Field(...)
    company: str = Field(...)
    password:str = Field(...)

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdulazeez@x.edu.ng",
                "designation": "Managing Director",
                "Company": "ABC company",
                "password": "Yourpasswordgoes here."
            }
        }

class UpdateUserModel(BaseModel):
    fullname: Optional[str]
    email: Optional[EmailStr]
    designation: Optional[str]
    company: Optional[str]
    password:Optional[str]

    class Config:
        schema_extra = {
            "example": {
                "fullname": "Abdulazeez Abdulazeez Adeshina",
                "email": "abdulazeez@x.edu.ng",
                "designation": "Managing Director",
                "Company": "ABC company",
                "password": "Yourpasswordgoes here."
            }
        }


def ResponseModel(data, message="Added Succesfully"):
    return {
        "data": [
            data
        ],
        "code": 200,
        "message": message,
    }


def ErrorResponseModel(error, code, message="Error adding user"):
    return {
        "error": error,
        "code": code,
        "message": message
    }