from fastapi import FastAPI
from app.controller.file_controller import router as file_router

app = FastAPI()

app.include_router(file_router, prefix="/file", tags=["file"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)