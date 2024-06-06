# Pydantic Models for the JWT Payload
from pydantic import BaseModel
from models.users import UserResponse


# Represents the user data we store in the JWT itself
# It's important to store the id so we can make DB calls
# without looking up the id in the users table


# This represents the payload stored inside the JWT
class JWTPayload(BaseModel):
    # The payload of the JWT
    user: UserResponse
    sub: str
    exp: int
