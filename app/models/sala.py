from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Sala(Base):
    __tablename__ = "salas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String, index=True)
    capacidad = Column(Integer)
    horario_inicio = Column(DateTime, default=datetime.datetime.utcnow)
    horario_fin = Column(DateTime, default=datetime.datetime.utcnow)
