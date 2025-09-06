from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import json
import uvicorn

from src.llm.item_generater import *

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get('/api/data')
async def create_item():
    try:
        item_text = await generate_item()
        return json.loads(item_text)
    except json.JSONDecodeError:
        return {"error": "Response of AI is not valid JSON format"}
    except Exception as e:
        return {"error": str(e)}


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)