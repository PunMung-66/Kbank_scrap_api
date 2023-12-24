import time
from fastapi import APIRouter
from gradio_client import Client

router = APIRouter(
    tags=["scrap"],
    responses={404: {"message": "Not found"}}
)
scrap_url = "https://punnawat01-gradio-scrap.hf.space"

@router.get('/statement/{name}')
async def statement_scrap_api(name:str):
    start = time.time()
    client = Client(scrap_url)
    result = client.predict(
                    name,	# str in 'parameter_8' Textbox component
                    fn_index=2
    )
    end = time.time()
    u_time = end - start
    return {"result" : result, "time" : u_time}

