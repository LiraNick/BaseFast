from typing import Union

from fastapi import FastAPI, HTTPException

from pydantic import BaseModel

from fastapi import status

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None

@app.get("/")
async def raiz():
    return {"Hello": "word"}

alunos = {

    1: {
        "nome" : "Lirinha",
        "idade" : 19,
        "email" : "nick@gmail"
        },
    2: {
        "nome" : "Jeffinho",
        "idade" : 23,
        "email" : "jeffbala@gmail"
        },
    3: {
        "nome" : "Cleitinho",
        "idade" : 32,
        "email" : "cleitola@gmail"
        },
    4: {
        "nome" : "Jasinto",
        "idade" : 16,
        "email" : "jaja@gmail"
        }

}


@app.get('/alunos')
async def get_alunos():
    return alunos

@app.get("/alunos/{alunos_id}")
async def get_aluno(alunos_id: int):
    aluno = alunos[alunos_id]
    alunos.update({"id" : alunos_id})
    try:
        aluno = alunos[alunos_id]
        alunos.update({'id':alunos_id})
        return pessoa
    except KeyError:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = 'aluno não encontrado')
    return aluno





if __name__ == '__main__':
    import uvicorn 

    uvicorn.run(
        "main:app",
        host = "127.0.0.1",
        port = 8000,
        log_level = "info",
        reload = True
    )

