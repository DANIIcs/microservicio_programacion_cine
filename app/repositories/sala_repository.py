from sqlalchemy.orm import Session
from app.models.sala import Sala

def obtener_salas(db: Session):
    return db.query(Sala).all()

def agregar_sala(db: Session, sala: Sala):
    db.add(sala)
    db.commit()
    db.refresh(sala)
    return sala

def obtener_sala_por_id(db: Session, sala_id: int):
    return db.query(Sala).filter(Sala.id == sala_id).first()

def eliminar_sala(db: Session, sala_id: int):
    sala = db.query(Sala).filter(Sala.id == sala_id).first()
    if sala:
        db.delete(sala)
        db.commit()
