from fastapi import FastAPI

app = FastAPI()

@app.get("/list")
async def list_all_documents():
    return {"message":"First FastAPI example"}