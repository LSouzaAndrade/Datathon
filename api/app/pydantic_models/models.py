from pydantic import BaseModel
from typing import List

class RecomendacaoRequest(BaseModel):
    historico_acessos: List[str]
    timestamp_acesso: int