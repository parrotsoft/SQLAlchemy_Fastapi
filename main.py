from fastapi import FastAPI
import uvicorn
import app.core.config as model

from app.core.config import engine

from app.routes.user_routes import router as user_routes
from app.routes.auth_routes import router as auth_routes
from app.routes.book_routes import router as book_routes

model.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mi App",
    description="Ejemplo CUL - Desarrollo Web II",
    version="1.0.0"
)


@app.get("/")
def index():
    return {
        "message": "Hola Mundo..."
    }


app.include_router(router=user_routes, tags=['Users'], prefix='/users')
app.include_router(router=auth_routes, tags=["Auth"], prefix="/auth")
app.include_router(router=book_routes, tags=["Books"], prefix="/books")

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="localhost",
                reload=True)
