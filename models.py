from sqlalchemy import Column, Integer, String, Float, Boolean, Date

from database import Base


class Aluno(Base):
    __tablename__ = "alunos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    plano = Column(String, nullable=False)  # Mensal, Trimestral ou Anual
    valor_mensalidade = Column(Float, nullable=False)
    data_matricula = Column(Date, nullable=False)
    ativo = Column(Boolean, default=True, nullable=False)