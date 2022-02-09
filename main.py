from fastapi import FastAPI, Form, status
from fastapi.responses import JSONResponse
import uvicorn

app = FastAPI()

# ルート
@app.get("/")
async def root():
    return {"message": "this is root"}

# 投稿機能を作る
@app.post("/posts")
async def post(name: str = Form(...)):
    return JSONResponse(content={"status": "ok", "name": name}, status_code=status.HTTP_201_CREATED)

# 起動
if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)
    