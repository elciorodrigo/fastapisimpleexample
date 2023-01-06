from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/{value}")
async def home(value: str):
    return {
        "message": "value is %s" % value
    }


if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8080)
