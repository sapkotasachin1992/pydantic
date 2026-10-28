from pydantic import BaseModel , Field ,field_validator,model_validator

class Register(BaseModel):
    username:str=Field(...,min_length=8)
    password:str
    re_password:str
    mobile:int
    @field_validator("mobile")  #helps to validate individual fields
    def  mobile_validator(cls,value):
        if len(str(value)) != 10 :
            raise ValueError("Mobile Number must be 10 digits")
        if str(value)[0] not in ['9','8','7']:
            raise ValueError("mobile number must be start from either 9 0r 7 or 8")
        return value
    
    @model_validator(mode="after")
    def pass_validator(self):
        if self.password != self.re_password:
            raise ValueError("Password does not match")
        if len(self.password) < 7:
            raise ValueError("password length must be greter than 6")

        return self

register=Register(username="sachin123",password="sachin",re_password="sachin",mobile=9111111111)

print(register)