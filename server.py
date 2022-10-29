# ===================== DOCUMENTATION ======================================
# Copyright (c) 2022-2022, Vitor Felipe Ramos Mello && Marcio Fossa Junior, VDEV.MarcioJR  - GGSS
#
# TESTING API
# PetStore API
#
from fastapi import FastAPI, Request, Response
from typing import List, Optional
from pydantic import BaseModel
from uuid import uuid4

app = FastAPI()

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