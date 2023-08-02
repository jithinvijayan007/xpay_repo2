from pydantic import BaseModel
from typing import Optional


class SignUpModel(BaseModel):
    fullname:str
    email:str
    phone:str
    profile_picture:str
    password:str
    is_active:Optional[bool]


    class Config:
        orm_mode=True
        schema_extra={
            'example':{
                "fullname":"jithink",
                "email":"jithin@gmail.com",
                "password":"testpass@123",
                "phone":"8888888888",
                "profile_picture":"s3_url_have_to_br_pass_here",
                "is_active":True
            }
        }