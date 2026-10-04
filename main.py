from fastapi import FastAPI

import models
from database import engine
from routers import alunos

# Cria as tabelas no SQLite caso ainda não existam
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="API Gestão de Academia", version="1.0.0")

app.include_router(alunos.router)