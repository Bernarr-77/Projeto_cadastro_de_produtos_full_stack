# python -m fastapi dev .\cadastro_produtos\main.py

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from itertools import count

class ProdutoInput(BaseModel):
    nome: str
    quantidade: int
    valor: float

class Produtos(ProdutoInput):
    id: int

lista_produtos = []

contador_id = count(1)

app = FastAPI()

@app.get("/produtos")
def buscar_produtos():
    return lista_produtos

@app.post("/produtos/")
def adicionar_produtos(Produto: ProdutoInput):
    novo_produto = Produtos(
        id= next(contador_id),
        nome=Produto.nome,
        quantidade= Produto.quantidade,
        valor= Produto.valor
        )
    lista_produtos.append(novo_produto)
    return novo_produto

@app.delete("/produtos/{id}")
def deletar_produtos(id: int):
    for index, produto in enumerate(lista_produtos):
        if produto.id == id:
            del lista_produtos[index]
            return {"mensagem": "Produto deletado com sucesso"}
        
    raise HTTPException(status_code=404, detail="Produto não encontrado")
        

