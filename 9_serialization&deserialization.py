from pydantic import BaseModel

class Students(BaseModel):
    name:str
    email:str
    age:int
    branch:str
    semester:int
    address:str

# this below are the data that come as api for eg from backend 
data={
    "name":"sachin",
    "email":"sachin@gmail.com",
    "age":12,
    "branch":"CSIT",
    "semester":6,
    "address":"Basundhara,KTM",
}
# student=Students(**data)
student=Students.model_validate(data)#doing this and above is same and this process is called deserialization

# print(student)

# now as we got student in key value form and we want to convert this into dictionary

print(student.model_dump())#converts pydantic class objects into dictionary .this is called serialization