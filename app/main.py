from fastapi import FastAPI
from .routers.user import user_router
from .database import engine


app = FastAPI()

app.include_router(user_router)

#===========================#

@app.on_event("startup")
async def startup():
    await engine.connect()
    

@app.on_event("shutdown")
async def shutdown():
    await engine.disconnect()