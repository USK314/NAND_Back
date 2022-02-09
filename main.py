from fastapi import FastAPI
import uvicorn

app = FastAPI()

# ルート
@app.get("/")
async def root():
    return {"message": "this is root"}

# 起動
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
    