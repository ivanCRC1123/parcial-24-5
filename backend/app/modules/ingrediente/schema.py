from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel


class IngredienteBase(SQLModel):
    nombre: str
    descripcion: Optional[str] = None


class IngredienteCreate(IngredienteBase):
    pass


class IngredienteUpdate(SQLModel):
    nombre: Optional[str] = None
    descripcion: Optional[str] = None


class IngredienteRead(IngredienteBase):
    id: int
    created_at: datetime
    updated_at: datetime


class IngredienteReadSimple(SQLModel):
    id: int
    nombre: str