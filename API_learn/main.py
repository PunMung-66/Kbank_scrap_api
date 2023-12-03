from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from bson import ObjectId

app = FastAPI()

client = MongoClient("mongodb://localhost:27017")
db = client["votes"]
collection = db["votes"]

class Vote(BaseModel):
    name: str
    count: int

@app.get("/")
async def root():
    return {"message": "Hello World"}

#Create
@app.post("/votes")
async def create_vote(vote: Vote):
    result = collection.insert_one(vote.dict())
    return {
        "id": str(result.inserted_id),
        "name": vote.name,
        "count": vote.count
    }

#Read
@app.get("/votes/{vote_id}")
async def get_vote(vote_id: str):
    vote = collection.find_one({"count": 2})
    if vote:
        return {
            "id": str(vote["_id"]),
            "name": vote["name"],
            "count": vote["count"]
        }
    else:
        raise HTTPException(status_code=404, detail="Vote not found")


@app.put("/votes/{vote_id}")
async def update_vote(vote_id: str, vote: Vote):
    result = collection.update_one(
        {"count": 2}, {"$set": vote.dict(exclude_unset=True)}
        )
    if result.modified_count == 1:
        return {"id": vote_id, "name": vote.name, "count": vote.count}
    else:
        raise HTTPException(status_code=404, detail="Vote not found")