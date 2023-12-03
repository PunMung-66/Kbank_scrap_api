from fastapi import FastAPI

app = FastAPI()


@app.get("/{x}/{y}")
async def root(x, y):
    sum = int(x) + int(y)
    return {"message": sum}
