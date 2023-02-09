""" from typing import Optional
from pydantic import BaseModel

class Aluno(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    email: str

alunos = [
    Aluno(id=1, nome="Andre", idade=25, email="andre@zuplae"),
    Aluno(id=2, nome="Vitor", idade=25, email="andre@zuplae")
]  """

from core.configs import settings
from core.database import engine
from models.aluno_models import AlunoModel
from models.usuario_models import UsuarioModel
from models.professor_models import ProfessorModel


print ("executando documento criar_tabelas")

async def create_tables():
    print("entrando na função")
    async with engine.begin() as conn:
        await conn.run_sync(settings.DB_BaseModel.metadata.drop_all)
        await conn.run_sync(settings.DB_BaseModel.metadata.create_all)
        print("Tabela Criada Com Sucesso!!!!")

if __name__ == "__main__":
    import asyncio 
    asyncio.run(create_tables())