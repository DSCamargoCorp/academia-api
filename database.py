from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Arquivo do banco SQLite (criado automaticamente na pasta do projeto)
SQLALCHEMY_DATABASE_URL = "sqlite:///./academia.db"

# check_same_thread=False é necessário no SQLite porque o FastAPI usa várias threads
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Cada requisição abre uma sessão própria
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Classe base de todos os models
Base = declarative_base()


def get_db():
    """Dependência: abre uma sessão e garante que ela seja fechada no final."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()