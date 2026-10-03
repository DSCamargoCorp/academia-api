# API Gestão de Academia (AlunosAcademia)

API RESTful para gerenciar alunos de uma academia, feita com **FastAPI**, **Pydantic** e **SQLAlchemy**, com persistência em **SQLite** e arquitetura modular em camadas.

Projeto de recuperação: Desenvolvimento e Defesa de API (Etec de Itaquera).
Autor: Daniel dos Santos Camargo

## Estrutura

```
projeto-recuperacao/
├── database.py      # engine, SessionLocal, Base e get_db
├── models.py        # modelo SQLAlchemy Aluno (tabela alunos)
├── schemas.py       # schemas Pydantic (entrada e resposta)
├── routers/
│   └── alunos.py    # APIRouter com o CRUD
├── main.py          # instância do FastAPI + create_all()
├── .gitignore
└── README.md
```

## Como executar

```bash
git clone https://github.com/DSCamargoCorp/academia-api.git
cd academia-api
python -m venv .venv
# Windows: .venv\Scripts\activate    |  Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt
fastapi dev main.py
```

Documentação interativa (Swagger): http://127.0.0.1:8000/docs

## Modelo Aluno

| Campo | Tipo | Regra |
|---|---|---|
| id | int | chave primária, gerado automaticamente |
| nome | str | obrigatório, 3 a 100 caracteres |
| email | str | obrigatório, formato válido, único |
| plano | str | `Mensal`, `Trimestral` ou `Anual` |
| valor_mensalidade | float | obrigatório, maior que 0 |
| data_matricula | date | obrigatório (AAAA-MM-DD) |
| ativo | bool | padrão `true` |

## Rotas

| Método | Rota | Descrição | Sucesso | Erros |
|---|---|---|---|---|
| POST | `/alunos/` | Cadastra um aluno | 201 Created | 400 (e-mail duplicado), 422 (validação) |
| GET | `/alunos/` | Lista alunos. Filtros opcionais: `plano`, `ativo`, `nome` | 200 OK | 422 |
| PUT | `/alunos/{id}` | Atualiza todos os campos | 200 OK | 404, 422 |
| DELETE | `/alunos/{id}` | Remove o aluno | 200 OK | 404 |

### Exemplo de corpo (POST / PUT)

```json
{
  "nome": "Maria Souza",
  "email": "maria@email.com",
  "plano": "Mensal",
  "valor_mensalidade": 99.9,
  "data_matricula": "2026-10-01",
  "ativo": true
}
```

### Exemplos de filtro

- `GET /alunos/?plano=Anual`
- `GET /alunos/?ativo=false`
- `GET /alunos/?nome=maria`