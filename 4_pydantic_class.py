# from pydantic import BaseModel


# class User(BaseModel):
#     user_id:int
#     name:str
#     age:int
#     is_active:bool

# user= User(user_id=1,name="sachin",age=12,is_active=True)


from pydantic import BaseModel,PositiveInt,StrictInt
from typing import List,Literal,Optional

class Orders(BaseModel):
    userId:PositiveInt
    productId:List
    payment_mode:Literal['online','cash']
    delivery_note:Optional[str]= None #this field is optional but if we receive date it must be string

order=Orders(userId=12,productId=[1,2,3],payment_mode="online")


print(order.productId)