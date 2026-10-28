from pydantic import BaseModel,computed_field

class CartItems(BaseModel):
    user_id:int
    product_id:int
    price:int
    quantity:int
    @computed_field
    @property #it sets or tells below method is actually like a property not function 
    def totalamount(self)-> int: # we have to always mention return type 
        return self.quantity*self.price

cart=CartItems(user_id=1,product_id=1,price=120,quantity=4)
print(cart)