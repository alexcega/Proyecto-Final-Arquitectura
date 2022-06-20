import os
from sqlalchemy import (
    MetaData,
    Column,
    Integer,
    String,
    Float,
    TIMESTAMP,
    Text,
    create_engine
)
from sqlalchemy.ext.declarative import declarative_base

#! Singleton
# Nos permite referenciar a la clase desde un solo punto
def get_postgres_uri():
    host = os.environ.get("DB_HOST", "postgres")
    port = 5432
    password = os.environ.get("DB_PASS", "abc123")
    user, db_name = "movies", "movies"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


Base = declarative_base(
    metadata=MetaData(),
)


engine = create_engine(
    get_postgres_uri(),
    isolation_level="REPEATABLE READ",
)

# !Directional Control
# La creacion de la base de datos se crea a partir de la metadata que recibe

#! Builder
#La clase nos permite crear un objeto con multiples atributos en pocos pasos

# Le agregue star cast
class Movie(Base):
    __tablename__ = "movies"

    movie_id = Column(Integer, primary_key=True)
    preference_key = Column(Integer)
    movie_title = Column(String)
    # star_cast = Column(String)
    rating = Column(Float)
    year = Column(Integer)
    create_time = Column(TIMESTAMP(timezone=True), index=True)

class User():
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String)
    password = Column(Integer)


def start_mappers():
    Base.metadata.create_all(engine)
