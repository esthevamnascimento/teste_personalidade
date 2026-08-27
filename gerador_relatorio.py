import os
import webbrowser
from datetime import datetime

def gerar_relatorio_html(nome, perfil, dados_perfil, metricas, status_unico, caminho_arquivo):
    data_atual = datetime.now().strftime("%d de %B, %Y")
    
    # Cálculos matemáticos para desenhar os gráficos do Dashboard
    traco_forte_nome = max(metricas.items(), key=lambda x: x[1][0])[1][1]
    traco_forte_valor = max(metricas.items(), key=lambda x: x[1][0])[1][0]
    
    media_intensidade = int(sum([info[0] for info in metricas.values()]) / 4)
    # Mapeia a porcentagem (0 a 100) para graus da agulha (-90 a 90)
    rotacao_agulha = (media_intensidade * 1.8) - 90 
    
    if media_intensidade < 60:
        status_intensidade = "FLEXÍVEL"
    elif media_intensidade < 75:
        status_intensidade = "MODERADO"
    else:
        status_intensidade = "ACENTUADO"

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>Relatório Psicométrico Individual - {nome}</title>
<style>
    /* Força o navegador a imprimir as cores de fundo nos gráficos */
    * {{
        -webkit-print-color-adjust: exact !important;
        print-color-adjust: exact !important;
    }}
    
    @media print {{
        .no-print {{ display: none !important; }}
        body {{ background: #fff; padding: 0; }}
        .page-container {{ box-shadow: none; border: none; padding: 0; width: 100%; }}
    }}
    
    body {{
        font-family: Arial, sans-serif;
        background-color: #f4f4f4;
        color: #333;
        margin: 0;
        padding: 20px;
        font-size: 12px;
    }}
    .page-container {{
        max-width: 850px;
        margin: 0 auto;
        background: #ffffff;
        padding: 30px;
        box-shadow: 0 0 10px rgba(0,0,0,0.1);
    }}
    
    /* CABEÇALHO (TABELA) */
    .header-table {{
        width: 100%;
        border-collapse: collapse;
        margin-bottom: 20px;
        border: 2px solid #d1d5db;
    }}
    .header-table th, .header-table td {{
        border: 1px solid #d1d5db;
        padding: 8px 12px;
        text-align: left;
    }}
    .header-table th.main-title {{
        background-color: #e2e8f0;
        text-align: center;
        font-size: 16px;
        padding: 15px;
        text-transform: uppercase;
    }}
    .header-table .label {{
        background-color: #f8fafc;
        font-weight: bold;
        font-style: italic;
        width: 15%;
        text-align: right;
    }}
    .header-table .value {{
        width: 35%;
    }}

    /* SEÇÕES E CAIXAS */
    .section-title {{
        background-color: #f1f5f9;
        border: 1px solid #d1d5db;
        padding: 10px;
        font-weight: bold;
        text-transform: uppercase;
        margin: 20px 0 10px 0;
    }}
    .content-box {{
        border: 1px solid #d1d5db;
        padding: 20px;
        margin-bottom: 20px;
    }}
    
    /* GRADE DO DASHBOARD */
    .dashboard-grid {{
        display: flex;
        justify-content: space-between;
        gap: 15px;
        margin-bottom: 15px;
    }}
    .dash-card {{
        flex: 1;
        border: 1px solid #d1d5db;
        padding: 15px;
        text-align: center;
        background: #fff;
    }}
    .dash-card-title {{
        font-size: 10px;
        color: #64748b;
        text-transform: uppercase;
        margin-bottom: 5px;
        letter-spacing: 1px;
    }}

    /* GRÁFICO 1: BARRA LINEAR */
    .linear-slider {{
        width: 100%;
        height: 8px;
        background: linear-gradient(to right, #22c55e, #eab308, #ef4444);
        border-radius: 4px;
        margin-top: 25px;
        position: relative;
    }}
    .slider-thumb {{
        width: 16px;
        height: 16px;
        background: #64748b;
        border: 2px solid #fff;
        border-radius: 50%;
        position: absolute;
        top: -6px;
        box-shadow: 0 0 4px rgba(0,0,0,0.3);
    }}
    .slider-labels {{
        display: flex;
        justify-content: space-between;
        font-size: 9px;
        color: #666;
        margin-top: 8px;
    }}

    /* GRÁFICO 2: VELOCÍMETRO */
    .half-donut {{
        width: 140px;
        height: 85px; /* Altura aumentada para não cortar o texto */
        position: relative;
        overflow: hidden;
        margin: 15px auto 0;
    }}
    .half-donut-bg {{
        width: 140px;
        height: 140px;
        border-radius: 50%;
        background: conic-gradient(from 270deg, #ef4444 0%, #ef4444 15%, #eab308 15%, #eab308 35%, #22c55e 35%, #22c55e 50%, transparent 50%);
        position: absolute;
    }}
    .half-donut-inner {{
        width: 90px;
        height: 90px;
        background: #fff;
        border-radius: 50%;
        position: absolute;
        top: 25px;
        left: 25px;
    }}
    .needle {{
        width: 3px;
        height: 55px;
        background: #1e293b;
        position: absolute;
        bottom: 15px;
        left: 68px;
        transform-origin: bottom center;
        border-radius: 3px 3px 0 0;
        z-index: 2;
    }}
    .needle::after {{
        content: '';
        width: 14px;
        height: 14px;
        background: #1e293b;
        border-radius: 50%;
        position: absolute;
        bottom: -5px;
        left: -5.5px;
    }}
    .gauge-value {{
        position: absolute;
        bottom: 0; /* Posição ajustada */
        width: 100%;
        text-align: center;
        font-weight: bold;
        font-size: 14px;
        z-index: 3;
        background: #fff; /* Fundo branco para sobrepor a base da agulha */
    }}

    /* GRÁFICO 3: ROSCA (DONUT) */
    .circular-chart {{
        width: 100px; /* Tamanho aumentado para não espremer */
        height: 100px;
        border-radius: 50%;
        margin: 10px auto;
        display: flex;
        align-items: center;
        justify-content: center;
    }}
    .circular-inner {{
        width: 76px;
        height: 76px;
        background: #fff;
        border-radius: 50%;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        line-height: 1.2; /* Ajuste do espaçamento entre as linhas */
    }}
    
    /* GRÁFICO DE BARRAS INFERIOR */
    .chart-container {{
        position: relative;
        padding: 20px 0;
    }}
    .axis-labels {{
        display: flex;
        justify-content: space-between;
        font-size: 10px;
        color: #666;
        margin-bottom: 10px;
        padding-left: 150px;
        padding-right: 50px;
    }}
    .center-line {{
        position: absolute;
        top: 30px;
        bottom: 0;
        left: calc(150px + 50%);
        width: 1px;
        border-left: 1px dashed #333;
        z-index: 1;
    }}
    .center-line-label {{
        position: absolute;
        top: 10px;
        left: calc(150px + 50%);
        transform: translateX(-50%);
        font-size: 9px;
        background: #fff;
        padding: 0 5px;
        color: #333;
    }}
    .bar-row {{
        display: flex;
        align-items: center;
        margin-bottom: 15px;
        position: relative;
        z-index: 2;
    }}
    .bar-label {{
        width: 140px;
        text-align: right;
        padding-right: 10px;
        font-weight: bold;
    }}
    .bar-track {{
        flex-grow: 1;
        background: #f1f5f9;
        height: 24px;
        position: relative;
        border: 1px solid #e2e8f0;
    }}
    .bar-fill {{
        height: 100%;
        background: #64748b;
    }}
    .bar-value {{
        width: 40px;
        text-align: left;
        padding-left: 10px;
        font-weight: bold;
    }}
    
    .btn-print {{
        display: block;
        width: 100%;
        padding: 15px;
        background: #0284c7;
        color: #fff;
        text-align: center;
        font-weight: bold;
        margin-top: 30px;
        cursor: pointer;
        border: none;
        border-radius: 6px;
    }}
</style>
</head>
<body>
    <div class="page-container">
        
        <!-- CABEÇALHO TABULAR -->
        <table class="header-table">
            <tr>
                <th colspan="4" class="main-title">Avaliação Psicométrica e Análise de Perfil</th>
            </tr>
            <tr>
                <td class="label">Avaliação</td>
                <td class="value">Teste de Personalidade (MBTI Modificado)</td>
                <td class="label">Data de conclusão</td>
                <td class="value">{data_atual}</td>
            </tr>
            <tr>
                <td class="label">Participante</td>
                <td class="value"><strong>{nome}</strong></td>
                <td class="label">Classificação</td>
                <td class="value"><strong>{status_unico}</strong></td>
            </tr>
            <tr>
                <td class="label">ID do relatório</td>
                <td class="value">MBTI-{datetime.now().strftime("%Y%m%d%H%M")}</td>
                <td class="label">Relatório por</td>
                <td class="value">Sistema Interno Automático</td>
            </tr>
        </table>

        <!-- RESUMO EXECUTIVO (DASHBOARD) -->
        <div class="section-title">Resumo Executivo</div>
        <div class="content-box" style="background: #f8fafc;">
            
            <!-- LINHA 1: CARDS DE TEXTO -->
            <div class="dashboard-grid">
                <div class="dash-card">
                    <div class="dash-card-title">Tipo Psicológico</div>
                    <div style="font-size: 24px; font-weight: bold; margin-top: 15px; color: #0f172a;">{perfil}</div>
                </div>
                <div class="dash-card">
                    <div class="dash-card-title">Arquétipo</div>
                    <div style="font-size: 18px; font-weight: bold; margin-top: 15px; color: #0284c7;">{dados_perfil['titulo']}</div>
                </div>
                <div class="dash-card">
                    <div class="dash-card-title">Traço Dominante</div>
                    <div style="font-size: 22px; font-weight: bold; margin-top: 15px; color: #0f172a;">{traco_forte_nome}</div>
                </div>
            </div>

            <!-- LINHA 2: CARDS GRÁFICOS -->
            <div class="dashboard-grid">
                <!-- GRÁFICO 1 -->
                <div class="dash-card">
                    <div class="dash-card-title">Classificação Geral</div>
                    <div style="font-size: 16px; font-weight: bold; margin-top: 10px; color: #0f172a;">{status_intensidade}</div>
                    
                    <div class="linear-slider">
                        <div class="slider-thumb" style="left: calc({media_intensidade}% - 8px);"></div>
                    </div>
                    <div class="slider-labels">
                        <span>Flexível</span>
                        <span>Moderado</span>
                        <span>Acentuado</span>
                    </div>
                </div>
                
                <!-- GRÁFICO 2 -->
                <div class="dash-card">
                    <div class="dash-card-title">Média de Consistência</div>
                    <div class="half-donut">
                        <div class="half-donut-bg"></div>
                        <div class="half-donut-inner"></div>
                        <div class="needle" style="transform: rotate({rotacao_agulha}deg);"></div>
                        <div class="gauge-value">{media_intensidade}%</div>
                    </div>
                </div>
                
                <!-- GRÁFICO 3 -->
                <div class="dash-card">
                    <div class="dash-card-title">Pico de Dominância</div>
                    <div class="circular-chart" style="background: conic-gradient(#0f172a {traco_forte_valor}%, #e2e8f0 {traco_forte_valor}% 100%);">
                        <div class="circular-inner">
                            <span style="font-size: 24px; font-weight: bold; color: #0f172a;">{traco_forte_valor}</span>
                            <span style="font-size: 10px; color: #64748b;">/ 100</span>
                        </div>
                    </div>
                </div>
            </div>
            
            <p style="text-align: center; margin: 10px 0 0 0; font-size: 14px;"><strong>Síntese do Perfil:</strong> {dados_perfil['resumo']}</p>
        </div>

        <!-- INTERPRETAÇÃO DO PERFIL -->
        <div class="section-title">Interpretação do Perfil</div>
        <div class="content-box">
            <p><strong>Comportamento Operacional:</strong><br>{dados_perfil['comportamento']}</p>
            <br>
            <p><strong>Diretrizes de Interação e Comunicação:</strong><br>{dados_perfil['como_agir']}</p>
        </div>

        <!-- PERFIL DIMENSIONAL (GRÁFICOS DE BARRA) -->
        <div class="section-title">Perfil Dimensional</div>
        <div class="content-box chart-container">
            <div class="center-line-label">Equilíbrio (50%)</div>
            <div class="center-line"></div>
            
            <div class="axis-labels">
                <span>0</span><span>10</span><span>20</span><span>30</span><span>40</span><span>50</span><span>60</span><span>70</span><span>80</span><span>90</span><span>100</span>
            </div>
            
            <div class="bar-row">
                <div class="bar-label">{metricas['E_I'][1]}</div>
                <div class="bar-track">
                    <div class="bar-fill" style="width: {metricas['E_I'][0]}%;"></div>
                </div>
                <div class="bar-value">{metricas['E_I'][0]}</div>
            </div>
            
            <div class="bar-row">
                <div class="bar-label">{metricas['S_N'][1]}</div>
                <div class="bar-track">
                    <div class="bar-fill" style="width: {metricas['S_N'][0]}%;"></div>
                </div>
                <div class="bar-value">{metricas['S_N'][0]}</div>
            </div>
            
            <div class="bar-row">
                <div class="bar-label">{metricas['T_F'][1]}</div>
                <div class="bar-track">
                    <div class="bar-fill" style="width: {metricas['T_F'][0]}%;"></div>
                </div>
                <div class="bar-value">{metricas['T_F'][0]}</div>
            </div>
            
            <div class="bar-row">
                <div class="bar-label">{metricas['J_P'][1]}</div>
                <div class="bar-track">
                    <div class="bar-fill" style="width: {metricas['J_P'][0]}%;"></div>
                </div>
                <div class="bar-value">{metricas['J_P'][0]}</div>
            </div>
        </div>
        
        <button class="btn-print no-print" onclick="window.print()">Salvar Documento em PDF</button>
    </div>
</body>
</html>"""

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    webbrowser.open("file://" + os.path.abspath(caminho_arquivo))