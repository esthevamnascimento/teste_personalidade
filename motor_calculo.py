# motor_calculo.py
from dados import PERGUNTAS, DESCRICOES_PERFIS

def calcular_perfil(respostas):
    pontuacoes = {"E": 0, "I": 0, "S": 0, "N": 0, "T": 0, "F": 0, "J": 0, "P": 0}
    
    for idx, resposta in enumerate(respostas):
        traco_avaliado = PERGUNTAS[idx]["traco"]
        pontuacoes[traco_avaliado] += resposta
        
    def calc_percent(t1, t2):
        total = pontuacoes[t1] + pontuacoes[t2]
        if total == 0: return 50, 50
        return round((pontuacoes[t1] / total) * 100), round((pontuacoes[t2] / total) * 100)
    
    perc_E, perc_I = calc_percent("E", "I")
    perc_S, perc_N = calc_percent("S", "N")
    perc_T, perc_F = calc_percent("T", "F")
    perc_J, perc_P = calc_percent("J", "P")
    
    perfil = ""
    perfil += "I" if perc_I >= perc_E else "E"
    perfil += "N" if perc_N >= perc_S else "S"
    perfil += "T" if perc_T >= perc_F else "F"
    perfil += "J" if perc_J >= perc_P else "P"
    
    dados_perfil = DESCRICOES_PERFIS.get(perfil, {
        "titulo": "Perfil não identificado",
        "resumo": "Padrão de respostas apresentou uma combinação atípica.",
        "comportamento": "Apresenta variação ampla dependendo do contexto situacional.",
        "como_agir": "Recomenda-se abordagem adaptativa."
    })
    
    metricas = {
        "E_I": (max(perc_E, perc_I), "Introversão" if perc_I >= perc_E else "Extroversão"),
        "S_N": (max(perc_S, perc_N), "Intuição" if perc_N >= perc_S else "Observação"),
        "T_F": (max(perc_T, perc_F), "Lógica" if perc_T >= perc_F else "Sentimento"),
        "J_P": (max(perc_J, perc_P), "Julgamento" if perc_J >= perc_P else "Percepção")
    }

    if "N" in perfil and "T" in perfil:
        status_unico = "Analista / Gestor (Estratégia e Lógica)"
    elif "N" in perfil and "F" in perfil:
        status_unico = "Diplomata / Criativo (Inovação e Pessoas)"
    elif "S" in perfil and "J" in perfil:
        status_unico = "Sentinela / Operacional (Processos e Execução)"
    else:
        status_unico = "Explorador / Suporte (Ação e Resolução Prática)"
    
    return perfil, dados_perfil, metricas, status_unico