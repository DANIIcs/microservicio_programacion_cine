from fastapi import FastAPI
from app.routes import sala_routes

app = FastAPI()

# Incluir las rutas del microservicio de programación de salas
app.include_router(sala_routes.router)

@app.get("/")
def root():
    return {"message": "Microservicio de programación de salas de cine"}
