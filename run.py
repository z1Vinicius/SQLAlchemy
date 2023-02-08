from infra.repository.filmes_repository import FilmesRepository
from infra.repository.atores_repository import AtoresRepository

repo = AtoresRepository()

# repo.insert('Doctor Who', 'Ficcão', 1964)
# repo.update('Teste', 'Cu123')
# repo.delete('Doctor Who2')

data = repo.select()

print(data)