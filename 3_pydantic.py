from pydantic import validate_call,StrictInt,PositiveInt
@validate_call
def generateMul(a:StrictInt,b:PositiveInt):
    return a+b

print(generateMul("ss",4))