from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.db.init_db import init_db,close_db
import uvicorn


@asynccontextmanager
async def lifespan(app: FastAPI):
    # ── Startup ──
    await init_db()
    yield
    # ── Shutdown ──
    await close_db()

app = FastAPI(
    title="Curator API",
    version="1.0.0",
    lifespan=lifespan,
)

@app.get('/')
def root():
    return {'message': 'Curator blog server is running'}



def start():
    uvicorn.run(app,host='127.0.0.1',port=8000, reload=True)