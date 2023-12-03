from fastapi import FastAPI
from routers import sum

app = FastAPI()

app.include_router(sum.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Scrapping API"}
