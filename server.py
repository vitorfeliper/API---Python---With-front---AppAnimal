from fastapi import FastAPI, Request, Response

app = FastAPI()


@app.get("/")
async def Home():
    return {"message": "Hello World"}