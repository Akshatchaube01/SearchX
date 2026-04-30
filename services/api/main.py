from fastapi import FastAPI

app = FastAPI(title="SearchX API")

@app.get("/")
def root():
    return {"status": "ok"}

@app.get("/health")
def health():
    return {"service": "searchx-api", "status": "healthy"}