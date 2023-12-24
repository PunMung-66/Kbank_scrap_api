from fastapi import APIRouter
from pymongo import MongoClient
from pydantic import BaseModel

client = MongoClient("mongodb+srv://admin:November@userdata.ipq1o58.mongodb.net/")

class login(BaseModel):
    name: str
    bank_u: str
    bank_p: str

class Pocket(BaseModel):
    Pocket: str
    Amount: int

class output_pocket(BaseModel):
    result: list[Pocket]

router = APIRouter(
    tags=["data"],
    responses={404: {"message": "Not found"}}
)


@router.get('/read_pocket/{name}')
async def read_data(name):
    db = client[name]
    col = db["Pocket"]
    print("--read--")
    if col.find_one() == None:
        return {"result" : f"Not found data in '{name}' account"}
    return (output_pocket(Your_pocket = col.find()))

@router.post('/login')
async def add_data_login(data: login):
    db = client[data.name]
    col = db["login"]
    if col.find_one({"name" : data.name}):
        return {"result" : "Your account already exists"}
    col.insert_one(data.dict())
    return {"result" : f"Add data login {data.name} completed"}

@router.post('/add_pocket/{name}')
async def add_pocket(name, pocket: Pocket):
    db = client[name]
    col = db["Pocket"]
    if col.find_one({"Pocket": pocket.Pocket}):
        return {"result" : f"'{pocket.Pocket}' pocket already exists"}
    col.insert_one(pocket.dict())
    return {"result" : f"Add '{pocket.Pocket}' pocket completed"}

@router.delete('/delete_pocket/{name}/{pocket_name}')
async def delete_pocket(name, pocket_name):
    db = client[name]
    col = db["Pocket"]
    if col.find_one({"Pocket": pocket_name}):
        col.delete_one({"Pocket": pocket_name})
        return {"result" : f"Delete '{pocket_name}' pocket completed"} #, output_pocket(Your_pocket = col.find())
    return {"result" : f"Not found '{pocket_name}' pocket"}

@router.delete('/logout/{name}')
async def logout(name):
    client.drop_database(name)
    return {"result" : f"Logout '{name}' completed"}

@router.put('/update_login/{name}')
async def update_login(name, data: login):
    db = client[name]
    col = db["login"]
    if col.find_one({"name" : data.name}):
        col.update_one({"name" : data.name}, {"$set" : {"bank_u" : data.bank_u, "bank_p" : data.bank_p}})
        return {"result" : f"Update '{data.name}' login completed"}
    return {"result" : f"Not found '{data.name}' account"}

@router.put('/update_pocket/{name}/{pocket_name}')
async def update_pocket(name, pocket_name, pocket: Pocket):
    db = client[name]
    col = db["Pocket"]
    if col.find_one({"Pocket" : pocket_name}):
        col.update_one({"Pocket" : pocket_name}, {"$set" : {"Amount" : pocket.Amount}})
        return {"result" : f"Update '{pocket_name}' pocket completed"}
    return {"result" : f"Not found '{pocket_name}' pocket"}