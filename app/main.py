import fastapi
from fastapi import FastAPI
from datetime import datetime



# create an app instance
app = FastAPI()

# metrics
requests = 0
pendings = 0
start_time = datetime.now()


@app.get("/")
def root():
    requests = requests + 1
    return {"Version": fastapi.__version__}


@app.get("/status")
def status():
    return {
        "current_requests": requests,
        "pending_requests": pendings,
        "total_uptime": datetime.now()-start_time,
        "health": "healthy"
    }