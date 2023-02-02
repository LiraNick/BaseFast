from fastapi import FastAPI

from fastapi import HTTPException

from fastapi import status

from models import Aluno

app = FastAPI()

@app.get('/')
async def raiz():
    return {"mensagem": "hello my friende"}

alunos = {

    1: {"nome" : "Lirinha", "idade" : 19, "email" : "nickporr@gmail"},
    2: {"nome" : "jasinto", "idade" : 12, "email" : "leite@gmail"},
    3: {"nome" : "tia", "idade" : 33, "email" : "romba@gmail"},
    4: {"nome" : "jeff", "idade" : 36, "email" : "jeffbala@gmail"}

}

@app.get('/alunos')
async def get_alunos():
    return alunos

@app.get('/alunos')
async def get_alunos():
    return alunos

#testanto commit
@app.get('/alunos/{alunos_id}')
async def read_item(alunos_id: int):
    aluno = alunos[alunos_id]
    alunos.update({'id': alunos_id})

    return aluno 

@app.get('/alunos/{alunos_id}')
async def read_item(alunos_id: int):
    try:
        aluno = alunos[alunos_id]
        alunos.update({'id':alunos_id})
        return aluno
    except KeyError:
        raise HTTPException(
            status_code = status.HTTP_404_NOT_FOUND, detail = 'Não encontramos'
        )

@app.post("/alunos", status_code=status.HTTP_201_CREATED)
async def post_aluno(aluno: Aluno):
    next_id: int = len(alunos) + 1
    alunos[next_id] = aluno
    del aluno.id
    return aluno

@app.put('/alunos/{alunos_id}')
async def put_aluno(aluno_id: int, aluno: Aluno):
    if aluno_id in alunos:
        alunos[aluno_id] = aluno
        return aluno
    else:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = 'Não encontramos')

if __name__ == 'main':
    import uvicorn

    uvicorn.run(
        "main:app",
        host = "127.0.0.1",
        port = 8000,
        log_level = "info",
        reload = True

    )
