from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class User(BaseModel):
    name: str
    password: str
    nombre: str
    apellido: str
    direccion: Optional[str]
    telefono: int
    email: str
    activo: bool
    created_at: datetime = datetime.now()
