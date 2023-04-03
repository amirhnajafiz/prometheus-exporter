import fastapi
from fastapi import FastAPI



# create an app instance
app = FastAPI()


@app.get("/")
def root():
    return {"Version": fastapi.__version__}


@app.get("/status")
def status():
    return {
        "current_requests": "",
        "pending_requests": "",
        "total_uptime": "",
        "health": "healthy"
    }