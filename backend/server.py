# ===================== DOCUMENTATION ======================================
# Copyright (c) 2022-2022, Vitor Felipe Ramos Mello && Marcio Fossa Junior, VDEV.MarcioJR - GGSS
# Universidade do Vale do Itajaí - Ciência Da Computação - Programação Web
# v0.1 - Criação da API
# v0.2 - Testes da API
# v0.3 - Entrega da API
# v0.4 - Consumo de API com frontend básico
# v0.6 - Atualização do frontend
# (current) v0.7 Atualização da documentação
#
#
#
#
#


from fastapi import FastAPI, Request, Response
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

# ========================== CORS ================================ #

origins = [
    'http://localhost:5500',
    'http://localhost:8080',
    'http://localhost:5000',
    'http://127.0.0.1:5500',
    'https://c73c-2804-7f5-d080-867c-c907-7279-ffb3-939d.ngrok.io',
    'https://a44a-2804-7f5-d080-867c-e586-1daa-b640-63c1.ngrok.io',
    'https://9377-2804-1b2-6043-bb9a-4059-bd58-eaae-66d1.ngrok.io',
    'https://26e1-2804-1b2-6043-bb9a-4059-bd58-eaae-66d1.ngrok.io',
    'https://9e83-2804-1b2-6043-bb9a-4059-bd58-eaae-66d1.ngrok.io',
    'https://f703-2804-1b2-6043-bb9a-4059-bd58-eaae-66d1.ngrok.io'
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins  ,
    allow_credentials=True ,
    allow_methods=["*"]    ,
    allow_headers=["*"]
)

# ================================================================ #
# ========================= ANIMAL MODEL ========================= #
class Animal(BaseModel):
    id: Optional[str]
    type: str
    name: str
    age: int
    sex: str
    color: str

database: List[Animal] = []

#========================== CRUD CREATE ============================#

@app.get('/animals')
async def ListAnimals():
    return database

# create
@app.post('/animals')
async def CreateAnimal(animal: Animal):
    animal.id = str(uuid4())
    database.append(animal)
    return None

#==================================================================#

#========================== CRUD DELETE ============================#
# delete
@app.delete('/animals/{animal_id}')
async def RemoveAnimal(animal_id: str):
    position = -1
    # Search animal index
    for index, animal in enumerate(database):
        if animal.id == animal_id:
            position = index
            break
    if position != -1:
        database.pop(position)
        return {'msg': 'Animal deleted successfully'}
    else:
        return {'error': 'Animal not found'}

#==================================================================#

#============================= GET ================================#

@app.get('/animals/{animal_id}')
async def GetAnimal(animal_id: str):
    for animal in database:
        if animal.id == animal_id:
            return animal
    return {'error': 'Animal not found'}

#==================================================================#