from infra.configs.connection import DBConnectionHandler
from infra.entities.filmes import Filmes

class FilmesRepository:
    def select(self):
        with DBConnectionHandler() as db:
            data = db.session.query(Filmes).all()
            return data
        
    def insert(self, titulo, genero, ano):
        with DBConnectionHandler() as db:
            data = Filmes(titulo = titulo, genero = genero, ano = ano)
            db.session.add(data)
            db.session.commit()
            
    def delete(self, titulo):
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).delete()
            db.session.commit()
            
    def update(self, titulo, newTitulo):
        with DBConnectionHandler() as db:
            db.session.query(Filmes).filter(Filmes.titulo == titulo).update({ "titulo": newTitulo })
            db.session.commit()