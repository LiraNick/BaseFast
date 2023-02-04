from typing import Optional
from pydantic import BaseModel, validator

class Aluno(BaseModel):
    id: Optional[int] = None
    nome: str
    idade: int
    email: str

    @validator('nome')
    def validar_nome(cls, value):
        abacate = value.split(' ')
        if len(abacate) < 3:
            raise ValueError('O Nome deve ter nome minimo 3 espacos')

alunos = [
    Aluno(id=1, nome="Andre vitor granemann", idade=25, email="andre@zuplae"),
    Aluno(id=2, nome="Vitor belli pereira", idade=25, email="andre@zuplae")
]