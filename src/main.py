import uvicorn
import os
import sys
from fastapi import FastAPI
from pydantic import BaseModel

arguments = sys.argv

reload = True if "--reload" in arguments else False

app = FastAPI()

'''
Event Types
'''


class Payload(BaseModel):
    class Config:
        extra = "allow"


class Body(BaseModel):
    eventId: str
    validTime: str
    payload: Payload


'''
Required Health Check
'''


@app.get("/health")
def health():
    return {}


'''
Transformer
'''


@app.post("/transform")
async def transform(body: Body):
    print("received body", body)
    return {"eventId": body.eventId, "validTime": body.validTime, **body.payload.model_dump()}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=int(os.environ["PORT"] if "PORT" in os.environ else 8000), log_level="info", reload=reload)
