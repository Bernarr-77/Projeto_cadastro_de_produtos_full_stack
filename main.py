# python -m fastapi dev .\cadastro_produtos\main.py

from fastapi import FastAPI,HTTPException,Depends
from schemas import ProdutoInput, Produtos
from database import init_db, get_db_connection
import sqlite3
from typing import List

init_db()

app = FastAPI()

@app.get("/produtos", response_model=List[Produtos])
def listar_produtos(conexao: sqlite3.Connection = Depends(get_db_connection)):
    try:
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtos")
        produtos = cursor.fetchall()
        return produtos
    except sqlite3.Error as error:
        raise HTTPException(status_code=404,detail=f"Erro no banco de dados: {str(error)}")

    

@app.post("/produtos/")
def adicionar_produtos(Produto: ProdutoInput, conexao: sqlite3.Connection = Depends(get_db_connection)):
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "INSERT INTO produtos (nome, quantidade, valor) VALUES(?, ?, ?)",
            (Produto.nome, Produto.quantidade, Produto.valor)
        )
        conexao.commit()
        novo_id = cursor.lastrowid
        return {"status": "Produto criado!", "id": novo_id, "dados": Produto.dict()}
    except sqlite3.Error as error:
        raise HTTPException(status_code=404,detail=f"Erro no banco de dados: {str(error)}")



# @app.delete("/produtos/{id}")
# def deletar_produtos(id: int):
#     for index, produto in enumerate(lista_produtos):
#         if produto.id == id:
#             del lista_produtos[index]
#             return {"mensagem": "Produto deletado com sucesso"}
        
#     raise HTTPException(status_code=404, detail="Produto não encontrado")


# @app.patch("/produtos/{item_id}")
# def atualizar_item(item_id: int, produto_atualizado: ProdutoInput):
#     for index, produto in enumerate(lista_produtos):
#         if produto.id == item_id:
#             if produto_atualizado.nome is not None:
#                 lista_produtos[index].nome = produto_atualizado.nome
#             if produto_atualizado.quantidade is not None:
#                 lista_produtos[index].quantidade = produto_atualizado.quantidade
#             if produto_atualizado.valor is not None:
#                 lista_produtos[index].valor = produto_atualizado.valor
            
#             return lista_produtos[index]
    
#     raise HTTPException(status_code=404, detail="Produto não encontrado")
               
