from ...database.database import Base
from sqlalchemy import Column, Integer, String, Uuid, DateTime, Boolean,ForeignKey
from datetime import datetime


class Venta(Base):
    __tablename__ = "ventas"
    id = Column(Uuid, primary_key=True)
    user_id=Column(String,ForeignKey("users.id",ondelete="CASCADE"))
    venta=Column(Integer)
    created_at = Column(DateTime, default=datetime.now(),
                        onupdate=datetime.now())
