                .join(Filmes, Atores.titulo_filme == Filmes.titulo)\
                .with_entities(
                    Atores.nome,
                    Filmes.genero,
                    Filmes.titulo,
                    Filmes.ano
                )\
                .all()
