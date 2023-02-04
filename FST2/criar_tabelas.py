from typing import Optional
from pydantic import BaseModel

class Aluno(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    email: str

alunos = [
    Aluno(id=1, nome="Andre", idade=25, email="andre@zuplae"),
    Aluno(id=2, nome="Vitor", idade=25, email="andre@zuplae")
]