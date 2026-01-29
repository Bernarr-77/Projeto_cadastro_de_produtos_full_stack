# python -m fastapi dev .\cadastro_produtos\main.py

from fastapi import FastAPI,HTTPException
from pydantic import BaseModel
from itertools import count
from typing import Optional

class ProdutoInput(BaseModel):
    nome: Optional[str] = None
    quantidade: Optional[int] = None
    valor: Optional[float] = None

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


@app.patch("/produtos/{item_id}")
def atualizar_item(item_id: int, produto_atualizado: ProdutoInput):
    for index, produto in enumerate(lista_produtos):
        if produto.id == item_id:
            if produto_atualizado.nome is not None:
                lista_produtos[index].nome = produto_atualizado.nome
            if produto_atualizado.quantidade is not None:
                lista_produtos[index].quantidade = produto_atualizado.quantidade
            if produto_atualizado.valor is not None:
                lista_produtos[index].valor = produto_atualizado.valor
            
            return lista_produtos[index]
    
    raise HTTPException(status_code=404, detail="Produto não encontrado")
               
