from typing import Optional, List

from sqlalchemy import create_engine, Column, Integer, String,Float, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///products.db', echo=True)
session = sessionmaker(bind=engine)

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    is_available = Column(Boolean, nullable=False, default=True)

class ProductRepository:
    def __init__(self, ses):
        self.session = ses

    def add(self, product: Product) -> None:
        self.session.add(product)
        self.session.commit()

    def delete(self, entity_id: int) -> None:
        product = self.session.query(Product).filter(Product.id == entity_id).first()
        if product:
            self.session.delete(product)
            self.session.commit()

    def get_all(self) -> List[Product]:
        return self.session.query(Product).all()

    def get_by_id(self, entity_id: int) -> Optional[Product]:
        return self.session.query(Product).filter(Product.id == entity_id).first()

    def update(self, new_product: str):
        product = self.session.query(Product).filter(Product.id == new_product.id).first()
        if product:
            product = new_product
            self.session.update(product)
            product.name = new_product.name
            product.price = new_product.price
            product.is_available = new_product.is_available
            self.session.execute(product)
with session() as s:
    pass



