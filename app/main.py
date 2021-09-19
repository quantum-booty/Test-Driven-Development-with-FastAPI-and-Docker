from fastapi import FastAPI, Depends
from app.config import get_settings, Settings

app = FastAPI()


@app.get('/ping')
def pong():
    return {'ping': 'pong!', 'environment': settings.environment}
