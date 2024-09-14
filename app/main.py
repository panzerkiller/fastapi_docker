from fastapi import FastAPI

app = FastAPI()

@app.get("/hello/{name}")
async def greeting(name: str):
    return {"greeting": f"Hello {name}, how are you today???"}