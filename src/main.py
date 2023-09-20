from fastapi import FastAPI
from pydantic import BaseModel

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
    return {"eventId": body.eventId, "validTime": body.validTime, **body.payload.dict()}
