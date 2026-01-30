from pydantic import BaseModel
from typing import Optional

class ProdutoInput(BaseModel):
    nome: str
    quantidade: Optional[int] = None
    valor: Optional[float] = None

class Produtos(ProdutoInput):
    id: int