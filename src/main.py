from fastapi import FastAPI

app = FastAPI(title="AI Tour")


@app.get("/")
async def hello_world():
    return {"message": "Hello world!"}