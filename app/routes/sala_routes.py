from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.repositories import sala_repository
from app.models.sala import Sala
from app.database import get_db

router = APIRouter(
    prefix="/salas",
    tags=["Salas"]
)

@router.get("/")
def listar_salas(db: Session = Depends(get_db)):
    return sala_repository.obtener_salas(db)

@router.post("/")
def crear_sala(sala: Sala, db: Session = Depends(get_db)):
    return sala_repository.agregar_sala(db, sala)

@router.get("/{sala_id}")
def obtener_sala(sala_id: int, db: Session = Depends(get_db)):
    sala = sala_repository.obtener_sala_por_id(db, sala_id)
    if sala is None:
        raise HTTPException(status_code=404, detail="Sala no encontrada")
    return sala

@router.delete("/{sala_id}")
def eliminar_sala(sala_id: int, db: Session = Depends(get_db)):
    sala_repository.eliminar_sala(db, sala_id)
    return {"message": "Sala eliminada exitosamente"}
