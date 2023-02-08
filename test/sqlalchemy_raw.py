from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

import warnings
from pprint import pprint

# Database Type and Driver
sqlDialect:str = 'mysql'
sqlDriver:str = 'pymysql'

# User and Password
sqlUser:str = 'root'
sqlPassword = ''

# SQL Port and Data Base
sqlPort:str = '3306'
sqlDB:str = 'cinema'

# Configurations 
sqlEngine = create_engine(f"{sqlDialect}+{sqlDriver}://{sqlUser}:{sqlPassword}@localhost:{sqlPort}/{sqlDB}")
Base = declarative_base()
Session = sessionmaker(bind = sqlEngine)
session = Session()

# Entities
class Filmes(Base): # Utilizar o nome da tabela 
    __tablename__ = "filmes" # Nome da tabela
    
    titulo = Column(String, primary_key = True) # Coluna título que é uma primary key
    genero = Column(String, nullable = False) # Coluna genero que não pode ser nula
    ano = Column(Integer, nullable = False) # Coluna ano que não pode ser nula
    
    def __repr__(self):
        return f"Filme (titulo = {self.titulo}, genero = {self.genero}, ano = {self.ano})"

# SQL

# Insert
testInsert = Filmes(titulo = 'A bela e a fera', genero = 'Romance', ano = 1890)
session.add(testInsert)
session.commit()

# Delete
session.query(Filmes).filter(Filmes.ano == 1890).delete()
session.commit()

# Update
session.query(Filmes).filter(Filmes.genero == 'Aventura').update({ "genero": "Comédia" })
session.commit()

# Select
data = session.query(Filmes).all()
# data = session.query(Filmes).filter(Filmes.ano == 2012).all()
pprint(data) # Print de toda a tabela
