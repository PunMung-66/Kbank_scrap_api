from fastapi import FastAPI, BackgroundTasks
import asyncio

app = FastAPI()

async def background_task(counter: int):
    while True:
        counter += 2
        print(f"Counter: {counter}")
        await asyncio.sleep(5)  # Sleep for 5 seconds

@app.get("/")
async def read_root(background_tasks: BackgroundTasks):
    # Start the background task when the root endpoint is accessed
    background_tasks.add_task(background_task, counter=0)
    return {"message": "Background task started"}
