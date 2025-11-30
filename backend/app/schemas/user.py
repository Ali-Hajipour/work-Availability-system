from pydantic import BaseModel, Field

#Registration schema input
class UserCreate(BaseModel):
    username : str = Field (..., min_length=3 , max_length=32)
    personal_number : int = Field(..., ge=100000 , le=999999)
    password : str = Field(... , min_length=8)
    role : str =Field (..., pattern = "^(employee|hr|admin)$")


    #Login schema input
    class UserLogin (BaseModel):
        personal_number : int = Field(..., ge=100000 , le=999999)
        passsword : str = Field(..., min_length=8)


#Public user model // the user others will see
class PublicUser(BaseModel):
    id : int
    personal_number : int
    role : str

    class Config:
        orm_mode = True


class UserInternal (BaseModel):
    username : str
    id : int
    personal_number : int
    role : str
    class Config :
        orm_mode = True

