
# BookStore

A API da BookStore é uma interface robusta e flexível projetada para gerenciar operações relacionadas a uma livraria virtual. Permitindo aos usuários acessar e manipular informações sobre livros, autores, categorias, etc, a API oferece uma experiência completa para todo o gerenciamento.

## Rodando os testes

Para rodar os testes, rode o seguinte comando

```bash
  coverage run -m pytest
```


## Rodando localmente

Clone o projeto

```bash
  git@github.com:adaosanto/bookstore.git
```

Instale as dependências

```bash
  poetry install
```

Execute as migrações

```bash
  poetry run python3 manage.py migrate
```

Inicie o servidor do django

```bash
  poetry run python3 manage.py runserver
```

Inicie o processo do Celery e Celery Beat Django

```bash
  poetry run celery -A bookStore worker --beat --scheduler django  -l INFO
```

Inicie o container do Redis

```bash
  docker compose up redis -d --build
```

> **Observação**
> Certifique-se que o DEBUG esteja setado como 1 (DEBUG=1) no arquivo .env
## Deploy

Para fazer o deploy desse projeto com o docker compose rode

```bash
  docker compose up -d --build
```

Após a cricação e execução dos containers, no container *web*, deverá ser executado os seguintes comandos:

* Cria migrações do banco de dados
    ```bash
    poetry run python3 manager.py migrate --no-input
    ```
* Faz coleção dos arquivos estáticos, útil para o swagger e redoc
    ```bash
    poetry run python3 manager.py collectstatic --no-input
    ```
## Variáveis de Ambiente

Para rodar esse projeto, você vai precisar adicionar as seguintes variáveis de ambiente no seu .env

`SECRET_KEY` `DEBUG` `DJANGO_ALLOWED_HOSTS` `SQL_ENGINE` `SQL_DATABASE` `SQL_PASSWORD` `SQL_HOST` 
`DATABASE` `DROPBOX_CLIENT_ID_APP_KEY` `DROPBOX_CLIENT_SECRET_APP_SECRET` `DROPBOX_CODE_AUTHORIZATION`
`DROPBOX_API_REFRESH_TOKEN` `DROPBOX_API_URL` `DBBACKUP_GPG_RECIPIENT` `CELERY_ENABLED` `CELERY_BROKER_URL` `CELERY_RESULT_BACKEND`

## Funcionalidades

- Interface Swagger
- Interface Redoc


## Autores

- [@adaosantos](https://www.github.com/adaosanto)

