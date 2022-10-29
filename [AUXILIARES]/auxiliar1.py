#import from package fastapi import class or calsses
import random
from pydantic import BaseModel
from fastapi import FastAPI, Request, Response

#methods
#{
    # GET     receive information from server
    # POST    send information to server
    # PUT     update information in server
    # DELETE  remove information from server
#}

app = FastAPI()

@app.get('/hello/{name}')
async def welcome(name: str = ""):
    text = f'Hello {name}, welcome to server'

    return {"message": text}

@app.get('/squareroot/{n}')
async def squareRoot(n: int = 1):
    returns = n * n
    text = f'The saquare root of {n} is {returns}'
    return {"message" : text}

# query route exemple /double?n=4 returns the function double with n = 4 as int
@app.get('/double')
async def double(n: int = 1):
    result = 2 * n
    return {"result" : f'Double of {n} is {result}'}

# query route exemple with multiple parameters exemple /area?with=50&height=100 --> 
# --> returns the function area with width = 50 as int and height = 100 as int


@app.get('/area')
async def area(width: int = 1, height: int = 1):
    a = width * height
    return {"Area" : f'Width {width} and height {height}, area is {a}'}


# endpoints
@app.get("/") # First Page Home
#app.get("/") will access the home function
# the home function will returns the json object
async def Home(): 
    return {
                "message 0": "Hello, world!",
                "message 1":"Testing"
           }

@app.get("/Profile")
async def Profile(): 
    return {
                "Nome"  : "Nome Name",
                "Email" : "Email Mail",
                "Senha" : "Senha Password"
           }

@app.post("/Profile")
async def Signup(): 
    return {
                "message" : "Login Success"
           }

@app.put("/Profile")
async def Update(): 
    return {
                "message" : "Updated Success"
           }

@app.delete("/Profile")
async def Remove(): 
    return {
                "message" : "Deleted with Success"
           }


# REQUEST BODY
class Product(BaseModel):
    id: int
    name: str
    price: float

# f'' to attach vars into the str

@app.post('/products')
async def products(product: Product):
    product.id = random.randrange(1, 10)
    return {'message': f'Produto (ID: {product.id} NOME: {product.name} - PREÇO: R${product.price}) foi cadastrado com sucesso!'}

