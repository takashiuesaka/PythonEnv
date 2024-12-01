from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests

app = FastAPI()

@app.get("/")
async def root():
    message = "Hello World"
    return {"message": f"{message}"}

### URLを受け取り、そのURLの内容を読み取り、その内容をAzure OpenAI Serviceを使って要約するAPI
class Request(BaseModel):
    url: str

@app.post("/summarize")
async def summarize(req: Request):
    url = req.url

    # URLの内容を読み取る処理
    try:
        response = requests.get(url)
        content = response.text
    except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=400, detail=f"Error fetching URL: {e}")

    # Azure OpenAI Serviceを使って要約する処理
