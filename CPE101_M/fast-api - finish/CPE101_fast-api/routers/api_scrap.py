import time
from fastapi import APIRouter
from gradio_client import Client

router = APIRouter(
    tags=["scrap"],
    responses={404: {"message": "Not found"}}
)

@router.get('/balance/{name}')
async def balance_scrap_api(name:str):
    start = time.time()
    client = Client("https://punnawat01-gradio-scrap.hf.space/")
    result = client.predict(
				name,	# str in 'parameter_3' Textbox component
				fn_index=0
                )
    end = time.time()
    u_time = end - start
    return {"API result" : result, "time" : u_time}

@router.get('/statement/{name}')
async def statement_scrap_api(name:str):
    start = time.time()
    client = Client("https://punnawat01-gradio-scrap.hf.space/")
    result = client.predict(
                    name,	# str in 'parameter_8' Textbox component
                    fn_index=1
    )
    end = time.time()
    u_time = end - start
    return {"API result" : result, "time" : u_time}

