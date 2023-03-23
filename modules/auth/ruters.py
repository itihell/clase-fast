from fastapi import APIRouter, Depends
from .schemas.user import User
from database.database import get_db
from sqlalchemy.orm import session
from .models import user

router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

users = []


@router.get("/all")
async def all(db: session = Depends(get_db)):
    rows = db.query(user.User).all()
    data = {
        "data": rows
    }

    return data


@router.post("/create")
async def create(payload: User, db: session = Depends(get_db)):
    newData = user.User(        
        name=payload.name,
        password=payload.password,
        nombre=payload.nombre,
        apellido=payload.apellido,
        direccion=payload.direccion,
        telefono=payload.telefono,
        email=payload.email,
        activo=payload.activo,
    )
    db.add(newData)
    db.commit()
    db.refresh(newData)
    data = {
        "message": "Usuario creado con éxito",
        "status": "ok",
        "code": "200",
        "data": newData
    }
    return data
