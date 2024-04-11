from fastapi import FastAPI
import uvicorn

import app.models as model
from app.Config import engine
from app.routes import router as router_crud


model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Tienda de libros",
    description="Ejemplo CUL",
    version="1.0.0"
)


@app.get("/")
def index():
    return {
        "message": "Hello"
    }


app.include_router(router=router_crud, tags=["CRUD"], prefix="/books")

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="localhost",
                reload=True)
