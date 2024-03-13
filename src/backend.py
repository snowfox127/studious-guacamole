from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
import uvicorn
from main import combine


app = FastAPI()
origins = [
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get("/")
def read_root():
    return {"Hello": "test"}

@app.get("/input/{name}")
def read_item(name:str):
    
    finalOut = combine(name)
    return finalOut





