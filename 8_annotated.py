from pydantic import BaseModel,Field
from typing import Annotated

class Users(BaseModel):
    name:Annotated[str,Field(..., min_length=8)]
    age:Annotated[int,Field(..., ge=18)]

user = Users(name="hello",age=19)