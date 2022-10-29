from fastapi import FastAPI, Request, Response

app = FastAPI()

@app.get("/") # First Page Home

async def root(): 
    return {
                "message 0": "Hello, world!",
                "message 1":"Testing"
           }
