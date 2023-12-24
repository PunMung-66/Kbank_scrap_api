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

class status(BaseModel):
    tag: str
    previous: float
    current: float
    goal: float
    summary: float
    daily: float
    usage_d: float
    statement: str = "no"


class output(BaseModel):
    result: list[Pocket]

class output_status(BaseModel):
    result: status

class output_login(BaseModel):
    result: list[str]

router = APIRouter(
    tags=["data"],
    responses={404: {"message": "Not found"}}
)


async def update_status_gs(name):
    db = client[name]
    col = db["Pocket"]
    sum_goal = 0
    if col.find_one() == None:
        return {"result" : f"Not found data in '{name}' account"}
    for i in col.find():
        sum_goal += i["Amount"]
    col = db["status"]
    if col.find_one() != None:
        col.update_one({"tag" :"status"},{"$set" : {"goal" : sum_goal}})
        col.update_one({"tag" :"status"},{"$set" : {"summary" : col.find_one()["current"] - sum_goal}})
    return "Update all status completed"

@router.get('/read_pocket/{name}')
async def read_data(name):
    db = client[name]
    col = db["Pocket"]
    print("--read--")
    if col.find_one() == None:
        return {"result" : f"Not found data in '{name}' account"}
    return (output(result = col.find()))

@router.get('/read_all_login')
async def read_data():
    dbs = client.list_database_names()
    all_login = []
    for name in dbs:
        if name == "admin" or name == "local" or name == "config":
            continue
        db = client[name]
        col = db["login"]
        if col.find_one() == None:
            continue
        all_login.append(col.find_one()["name"])
    return (output_login(result = all_login))

@router.get('/read_status/{name}')
async def read_status(name):
    db = client[name]
    col = db["status"]
    if col.find_one() == None:
        return {"result" : f"Not found data in '{name}' account"}
    return (output_status(result = col.find_one()))


@router.post('/login')
async def add_data_login(data: login):
    db = client[data.name]
    col = db["login"]
    if col.find_one({"name" : data.name}):
        return {"result" : "Your account already exists"}
    col.insert_one(data.dict())
    col = db["status"]
    col.insert_one(status(tag = "status", previous = 0,current = 0, goal = 0, summary = 0, daily = 0, usage_d = 0).dict())
    return {"result" : f"Add data login {data.name} completed"}

@router.post('/add_pocket/{name}')
async def add_pocket(name, pocket: Pocket):
    db = client[name]
    col = db["login"]
    if col.find_one() == None:
        return {"result" : f"Not found data in '{name}' account"}
    col = db["Pocket"]
    if col.find_one({"Pocket": pocket.Pocket}):
        return {"result" : f"'{pocket.Pocket}' pocket already exists"}
    col.insert_one(pocket.dict())
    return {"result" : f"Add '{pocket.Pocket}' pocket completed", "status" : await update_status_gs(name)}

@router.delete('/delete_pocket/{name}/{pocket_name}')
async def delete_pocket(name, pocket_name):
    db = client[name]
    col = db["Pocket"]
    if col.find_one({"Pocket": pocket_name}):
        col.delete_one({"Pocket": pocket_name})
        return {"result" : f"Delete '{pocket_name}' pocket completed", "status" : await update_status_gs(name)} 
    return {"result" : f"Not found '{pocket_name}' pocket"}

@router.delete('/logout/{name}')
async def logout(name):
    client.drop_database(name)
    return {"result" : f"Logout '{name}' completed"}

@router.put('/set_daily/{name}/{daily}')
async def set_daily(name, daily: float):
    db = client[name]
    col = db["status"]
    if col.find_one() == None:
        return {"result" : f"Not found data in '{name}' account"}
    col.update_one({"tag" :"status"},{"$set" : {"daily" : daily}})
    return {"result" : f"Set daily to {daily} per day completed"}

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
        col.update_one({"Pocket" : pocket_name}, {"$set" : {"Pocket" : pocket.Pocket}})
        return {"result" : f"Update '{pocket.Pocket}' pocket completed", "status" : await update_status_gs(name)}
    return {"result" : f"Not found '{pocket_name}' pocket"}