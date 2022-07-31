from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def main():
    return {"key": "Hello"}


if __name__ == '__main__':
    uvicorn.run(
        "main:app",
        port=5000,
        log_level="info",
        debug=True,
        reload=True
    )