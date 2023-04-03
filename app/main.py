import fastapi
from fastapi import FastAPI



# create an app instance
app = FastAPI()


@app.get("/")
def root():
    return {"Version": fastapi.__version__}