from models import *
from fastapi import FastAPI
from fastapi import HTTPException




app = FastAPI(title="Random proxy")

with db:
    db.create_tables([Proxy])

print('DONE')


@app.get(
    "/",
    response_description="Random proxy",
    description="Get random proxy from database",
    response_model=Proxy,
)
async def get():
    try:
        proxy = db.get(db.get_random())
    except IndexError:
        raise HTTPException(404, "Phrase list is empty")
    return proxy






# @app.get('/')
# def home():
#     return {"key": "Hello"}

# @app.get('/{pk}')
# def get_item(pk: int, q: int = None):
#     return {"key": pk, "q": q}
