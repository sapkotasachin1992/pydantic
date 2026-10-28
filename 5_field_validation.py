from pydantic import BaseModel,PositiveInt,StrictInt,Field
from typing import List,Optional,Literal


class Employee(BaseModel):
    name:str = Field(
        ...,  #this means field is required
        min_length=6,
        max_length=20,
        description="Employee Name"
    )
    salary:PositiveInt = Field(
        ...,
        ge=20000,
        le=140000
    )

    email:str = Field(
        default=""
    )

# employee=Employee(name="abc",salary=5)   practically it wrong as name can not be abc and salary cannot be rs 5
emplyee1=Employee(name="sachin",salary=30000,email="sachin@gmail.com")

print(emplyee1)
