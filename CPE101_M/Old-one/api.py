from fastapi import FastAPI
from routers import api_scrap, api_database

app = FastAPI()

app.include_router(api_scrap.router)
app.include_router(api_database.router)

@app.get("/")
async def root():
    return {"message": "Money_management_API"}