from sqlalchemy import ForeignKey, String, create_engine, select, Integer
from sqlalchemy.orm import DeclarativeBase, Mapped, Mapper, Session, mapped_column, relationship, sessionmaker
from typing import List, Optional
from datetime import date

class Base(DeclarativeBase):
    pass

class Author(Base):
    __tablename__ = 'authors'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(50), nullable=False)

    books:Mapped[List["Book"]] = relationship(back_populates="author", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Author {self.name}>"

class Book(Base):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    year: Mapped[Optional[int]] = mapped_column(Integer, nullable=True)

    author_id:Mapped[int] = mapped_column(Integer, ForeignKey("authors.id"))
    author:Mapped["Author"] = relationship(back_populates="books")

    def __repr__(self):
        return f"<Book: {self.title} - {self.author.name}>"

engine = create_engine('sqlite:///memory.db', echo=False)
Base.metadata.create_all(engine)

# with Session(engine) as session:
#     book1 = Book(title="Основание", year=1925)
#     book2 = Book(title="Я робот", year=1920)
#     author1 = Author(name="Айзек Азимов", books=[book1, book2])
#
#     session.add(author1)
#     session.commit()

# with Session(engine) as session:
#     stm = select(Author).where(Author.name.like("%Айзек%"))
#     author = session.execute(stm).scalar_one_or_none()
#     print(author)
#
#     stm = select(Book).where(Book.title.like("%Основание%"))
#     book = session.execute(stm).scalar_one_or_none()
#     print(book)

# with Session(engine) as session:
#     stm = select(Author).where(Author.name.like("%Азимов%"))
#     author = session.execute(stm).scalars().first()
#     if author:
#         print(author)

with Session(engine) as session:
    book = session.execute(select(Book).where(Book.title == "Основание")).scalar_one_or_none()
    if book:
        session.delete(book)
        session.commit()




