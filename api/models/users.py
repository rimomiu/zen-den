from pydantic import BaseModel


class UserRequest(BaseModel):
#Represents a the parameters needed to create a new user
    username: str
    password: str
    first_name: str
    last_name: str
    email: str


class UserResponse(BaseModel):
    #Represents a user, with the password not included
    username: str
    first_name: str
    last_name: str
    email: str
    user_id: int
    admin: bool
    #this is what is returned to the user, they will see it


class UserWithPw(UserRequest):
    #Represents a user with password included
    user_id: int
    admin: bool
    #used to verify when the user is logging in
