from database.database import Base
from sqlalchemy import Column, Integer, String, Uuid, DateTime, Boolean
from datetime import datetime
import uuid


class User(Base):
    __tablename__ = "users"
    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    nombre = Column(String, nullable=False)
    apellido = Column(String, nullable=False)
    direccion = Column(String, nullable=False)
    telefono = Column(Integer, nullable=True)
    email = Column(String, nullable=False, unique=True)
    activo = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.now(),
                        onupdate=datetime.now())
