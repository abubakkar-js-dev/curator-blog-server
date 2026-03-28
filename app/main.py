from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def root():
    return {'message': 'Curator blog server is running'}




def start():
    uvicorn.run(app,host='127.0.0.1',port=8000, reload=True)