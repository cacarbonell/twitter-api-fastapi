
#fastapi
from fastapi import FastAPI

app = FastAPI()

@app.get(path="/")
def home():
    """
    Home
    
    This is point start the app
    """
    return {"Twitter API": "Working!"}
