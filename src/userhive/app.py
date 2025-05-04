"""FastAPI application for UserHive API."""

from fastapi import FastAPI

app = FastAPI(title="UserHive API")


@app.get("/")
async def hello_world():
    """Return a simple hello world message."""
    return {"message": "helloworld"}


@app.get("/hello")
async def hello():
    """Return a simple hello world message."""
    return {"message": "helloworld"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
