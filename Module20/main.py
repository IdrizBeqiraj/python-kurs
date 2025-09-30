from fastapi import FastAPI

app = FastAPI()
@app.get ("/")

def root():
    return  {"Message" : "HelloWorld"}

@app.get("/greet")

def read_root(name: str):
    return {"Message": "f'Hello, {name}!'"}
