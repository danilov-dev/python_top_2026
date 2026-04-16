from sqlalchemy import ForeignKey, String, create_engine, select, Integer, Float
from sqlalchemy.orm import DeclarativeBase, Mapped, Mapper, Session, mapped_column, relationship, sessionmaker
from typing import List, Optional
from datetime import date

class Base(DeclarativeBase):
    pass

class Manufacturer(Base):
    __tablename__ = 'manufacturers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    country: Mapped[str] = mapped_column(String(150))

    products: Mapped[List["Product"]] = relationship(back_populates="manufacturer")

class Product(Base):
    __tablename__ = 'products'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)
    category: Mapped[str] = mapped_column(String(150), nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False, default=0)
    price: Mapped[float] = mapped_column(Float, nullable=False, default=0)

    manufacturer_id: Mapped[int] = mapped_column(Integer, ForeignKey('manufacturers.id'))
    manufacturer: Mapped["Manufacturer"] = relationship(back_populates="products")

    customer_id: Mapped[int] = mapped_column(Integer, ForeignKey('customers.id'))
    customer: Mapped["Costumer"] = relationship(back_populates="products")

class Customer(Base):
    __tablename__ = 'customers'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(150), nullable=False)

    products: Mapped[List["Product"]] = relationship(back_populates="customer")