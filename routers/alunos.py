from typing import List, Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models
import schemas
from database import get_db

router = APIRouter(prefix="/alunos", tags=["Alunos"])


@router.post("/", response_model=schemas.AlunoResponse, status_code=status.HTTP_201_CREATED)
def criar_aluno(aluno: schemas.AlunoCreate, db: Session = Depends(get_db)):
    if db.query(models.Aluno).filter(models.Aluno.email == aluno.email).first():
        raise HTTPException(status_code=400, detail="E-mail já cadastrado")
    novo = models.Aluno(**aluno.model_dump())
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo


@router.get("/", response_model=List[schemas.AlunoResponse])
def listar_alunos(
    plano: Optional[str] = None,
    ativo: Optional[bool] = None,
    nome: Optional[str] = None,
    db: Session = Depends(get_db),
):
    query = db.query(models.Aluno)
    if plano is not None:
        query = query.filter(models.Aluno.plano == plano)
    if ativo is not None:
        query = query.filter(models.Aluno.ativo == ativo)
    if nome is not None:
        query = query.filter(models.Aluno.nome.ilike(f"%{nome}%"))
    return query.all()