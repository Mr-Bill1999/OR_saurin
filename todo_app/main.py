from fastapi import FastAPI
from app.database import Base, engine
from app.routes import router


Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=80, reload=True)
