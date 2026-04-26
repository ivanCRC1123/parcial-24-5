from sqlmodel import Session, select
from app.modules.producto.model import Producto
from sqlalchemy.orm import selectinload


class ProductoService:

    def __init__(self, session: Session):
        self.session = session

    def get_all(self):
        statement = (
            select(Producto)
            .options(
                selectinload(Producto.categorias),
                selectinload(Producto.ingredientes)
            )
        )
        return self.session.exec(statement).all()

    def get_by_id(self, producto_id: int):
        statement = (
            select(Producto)
            .where(Producto.id == producto_id)
            .options(
                selectinload(Producto.categorias),
                selectinload(Producto.ingredientes)
            )
        )
        return self.session.exec(statement).first()

    def create(self, producto: Producto):
        self.session.add(producto)
        self.session.commit()
        self.session.refresh(producto)
        return producto

    def update(self, db_producto: Producto, data: dict):
        for key, value in data.items():
            setattr(db_producto, key, value)

        self.session.add(db_producto)
        self.session.commit()
        self.session.refresh(db_producto)
        return db_producto

    def delete(self, db_producto: Producto):
        self.session.delete(db_producto)
        self.session.commit()
    
    def get_filtered(self, min_precio, max_precio, limit, offset):
        statement = (
            select(Producto)
            .options(
                selectinload(Producto.categorias),
                selectinload(Producto.ingredientes)
            )
            .where(
                Producto.precio_base >= min_precio,
                Producto.precio_base <= max_precio
            )
            .offset(offset)
            .limit(limit)
        )
        return self.session.exec(statement).all()
