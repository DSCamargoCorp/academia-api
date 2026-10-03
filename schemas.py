from datetime import date
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class AlunoBase(BaseModel):
    nome: str = Field(..., min_length=3, max_length=100)
    email: str = Field(..., pattern=r"^[^@\s]+@[^@\s]+\.[^@\s]+$")
    plano: Literal["Mensal", "Trimestral", "Anual"]
    valor_mensalidade: float = Field(..., gt=0)
    data_matricula: date
    ativo: bool = True


class AlunoCreate(AlunoBase):
    """Entrada (POST e PUT): todos os campos são obrigatórios, exceto 'ativo'."""
    pass


class AlunoResponse(AlunoBase):
    """Saída: inclui o id gerado pelo banco."""
    id: int

    model_config = ConfigDict(from_attributes=True)