from fastapi import FastAPI 

from fastapi import HTTPException, status
from models import Aluno, alunos
from fastapi import Response
from typing import Optional, Dict, List, Any
from fastapi import Path, Query, Header, Depends
from time import sleep


app = FastAPI(
    title='MoreDevs2Blu',
    version='007',
    description='Desenvolvido Pela Melhor turma da historia'
)
def db():
    try:
        print('conexao com banco')
        sleep(1)
    finally:
        print('conexao com banco')
        sleep(1)

@app.get('/')
async def raiz():
    return { "mensagem": "Seja bem vindo ao more devs" }



@app.get('/alunos', 
description='lista de todos os alunos',
summary='retorno substantivo',
response_description="Lista de Alunos cadastrados"
 )
async def get_alunos(): 
    return alunos
@app.get('/alunos/{aluno_id}')
async def get_aluno(aluno_id: int = Path(default=None, title='ID Aluno', description='deve ser entre 1 ou 2', gt=0, lt=3), db :Any =Depends(db)): 
    try:
        aluno = alunos[aluno_id]
        return aluno

    except KeyError:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail='Aluno nao encontrado'
        )

@app.post('/alunos', status_code=status.HTTP_201_CREATED)
async def post_aluno(aluno: Aluno):
    next_id : int = len(alunos) +1
    alunos.id = next_id
    alunos.append(aluno)
    
    return aluno



@app.put('/alunos/{aluno_id}')
async def put_aluno(aluno_id: int, aluno: Aluno):
    
    if aluno_id in alunos:
        alunos[aluno_id] = aluno
        del aluno.id
        return aluno
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Aluno nao encontrado com este id {aluno_id}')


@app.delete('/alunos/{aluno_id}')
async def delete_aluno(aluno_id: int):
    
    if aluno_id in alunos:
        del alunos[aluno_id]
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Aluno nao encontrado com este id {aluno_id}')


@app.get('/calculadora')
async def calcular(a: int = Query(default=None, gt=5), b: int = Query(default=None, gt=5),  c:  Optional[int] = None, xdevs: str =Header(default=None)): 
    soma = a + b 
    if c:
        soma = soma + c
    print(f'devs: {xdevs}')
    return soma


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(
        "main:app",
        host= "127.0.0.1",
        port=8000,
        log_level = "info",
        reload = True
    )