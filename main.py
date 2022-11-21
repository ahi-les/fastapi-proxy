from fastapi import FastAPI

from api import router





app = FastAPI(title="Random proxy")
app.include_router(router)

