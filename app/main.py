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
    global requests

    requests = requests + 1
    return {"Version": fastapi.__version__}


@app.get("/status")
def status():
    global requests, pendings, start_time
    
    return {
        "current_requests": requests,
        "pending_requests": pendings,
        "total_uptime": datetime.now()-start_time,
        "health": "healthy"
    }