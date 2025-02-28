import math
import pandas as pd
import pickle
from app.pydantic_models.models import RecomendacaoRequest
from fastapi import APIRouter
from sklearn.metrics.pairwise import cosine_similarity


router = APIRouter()

df_noticias = pd.read_parquet('api/app/auxiliar/processed_itens.parquet')

with open("api/app/auxiliar/tfidf_vocab.pkl", "rb") as f:
    vectorizer = pickle.load(f)

with open("api/app/auxiliar/tfidf_matrix.pkl", "rb") as f:
    tfidf_matrix = pickle.load(f)


def recomendar_noticias(noticia_input, timestamp_acesso):
    """
    Função para recomendar notícias a partir de uma notícia de entrada.

    Parâmetros:
    - noticia_input: texto da notícia para comparar;
    - timestamp_acesso: timestamp (em segundos) do acesso para limitar as notícias recentes;

    Retorna:
    - DataFrame com as recomendações (notícia e similaridade).
    """
    JANELA_NOTICIAS = 7
    TOP_N = 5

    timestamp_limite = timestamp_acesso - JANELA_NOTICIAS * 24 * 60 * 60
    df_recentes = df_noticias[(timestamp_acesso >= df_noticias['issued']) & (df_noticias['issued'] >= timestamp_limite)].copy()
    tfidf_matrix_recentes = tfidf_matrix[df_recentes.index, :]

    input_tfidf = vectorizer.transform([noticia_input])
    similaridades = cosine_similarity(input_tfidf, tfidf_matrix_recentes).flatten()

    similar_indices_rel = similaridades.argsort()
    similar_indices_rel = similar_indices_rel[-TOP_N-1:]
    similar_indices_rel = similar_indices_rel[::-1]
    similar_indices_rel = similar_indices_rel[1:]

    indices_originais = df_recentes.index[similar_indices_rel]
    recomendacoes = pd.DataFrame({
        'noticia': df_noticias.loc[indices_originais, 'page'].values,
        'similaridade': similaridades[similar_indices_rel]
    })

    return recomendacoes

def analisar_historico(id_noticias):
    """
    Função para percorrer todas notícias do histórico do usuário.

    Parâmetros:
    - id_noticias: Array com os IDs das notícias acessadas;

    Retorna:
    - DataFrame com as recomendações para o histórico.
    """
    PESO_DECAIMENTO = 0.1
    TOP_N = 5

    rank_recomendacoes = pd.DataFrame()
    for i, id_noticia in enumerate(id_noticias):
        noticia = df_noticias.loc[df_noticias['page'] == id_noticia, 'noticia'].values[0]
        timestamp = df_noticias.loc[df_noticias['page'] == id_noticia, 'issued'].values[0]
        recomendacoes = recomendar_noticias(noticia, timestamp)
        recomendacoes['similaridade'] = recomendacoes['similaridade'] * math.exp(-PESO_DECAIMENTO * i)
        rank_recomendacoes = pd.concat([rank_recomendacoes, recomendacoes], ignore_index=True)
    rank_recomendacoes = rank_recomendacoes.sort_values(by='similaridade', ascending=False)

    return rank_recomendacoes['noticia'].head(TOP_N).values

@router.post("/recomendacoes")
def get_recomendacoes(request: RecomendacaoRequest):
    recomendacoes_array = analisar_historico(id_noticias=request.historico_acessos)
    recomendacoes = {"recomendacoes": recomendacoes_array.tolist()}
    return recomendacoes