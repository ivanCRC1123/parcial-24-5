from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, Path, Query
from sqlmodel import Session

from app.core.database import get_session
from app.modules.producto.model import Producto
from app.modules.producto.schema import ProductoCreate, ProductoRead, ProductoUpdate
from app.modules.producto.service import ProductoService

router = APIRouter(prefix="/productos", tags=["Productos"])


def get_service(session: Session = Depends(get_session)):
    return ProductoService(session)


@router.get("/", response_model=list[ProductoRead])
def get_all(
    service: Annotated[ProductoService, Depends(get_service)],
    min_precio: Annotated[float, Query(ge=0, description="Precio mínimo")] = 0,
    max_precio: Annotated[float, Query(ge=0, description="Precio máximo")] = 100000,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
    offset: Annotated[int, Query(ge=0)] = 0,
):
    return service.get_filtered(min_precio, max_precio, limit, offset)


@router.get("/{producto_id}", response_model=ProductoRead)
def get_by_id(
    service: Annotated[ProductoService, Depends(get_service)],
    producto_id: Annotated[int, Path(gt=0)],
):
    producto = service.get_by_id(producto_id)

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return producto


@router.post("/", response_model=ProductoRead, status_code=201)
def create(
    data: ProductoCreate,
    service: Annotated[ProductoService, Depends(get_service)],
):
    producto = Producto(**data.model_dump())
    return service.create(producto)


@router.put("/{producto_id}", response_model=ProductoRead)
def update(
    service: Annotated[ProductoService, Depends(get_service)],
    data: ProductoUpdate,
    producto_id: Annotated[int, Path(gt=0)],
):
    producto = service.get_by_id(producto_id)

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    return service.update(producto, data.model_dump(exclude_unset=True))


@router.delete("/{producto_id}", status_code=204)
def delete(
    service: Annotated[ProductoService, Depends(get_service)],
    producto_id: Annotated[int, Path(gt=0)],
):
    producto = service.get_by_id(producto_id)

    if not producto:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

    service.delete(producto)
    return
