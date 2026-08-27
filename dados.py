# banco_dados.py

PERGUNTAS = [
    {"texto": "Sinto-me energizado após passar tempo com um grupo grande de pessoas.", "traco": "E"},
    {"texto": "Prefiro conversas profundas com uma pessoa a interagir com várias em um evento social.", "traco": "I"},
    {"texto": "Geralmente tomo a iniciativa de me apresentar a novas pessoas em um ambiente desconhecido.", "traco": "E"},
    {"texto": "Necessito de um período de isolamento para recuperar energia após eventos sociais prolongados.", "traco": "I"},
    {"texto": "Tenho facilidade em articular meus pensamentos verbalmente de forma imediata.", "traco": "E"},
    {"texto": "Prefiro estruturar mentalmente minhas ideias antes de verbalizá-las ou opinar.", "traco": "I"},
    {"texto": "Sinto-me confortável sendo o centro das atenções em situações interpessoais.", "traco": "E"},
    {"texto": "Meu momento ideal de descanso envolve atividades individuais, como leitura ou consumo de mídia.", "traco": "I"},

    {"texto": "Tomo decisões baseando-me prioritariamente em dados empíricos e experiências práticas.", "traco": "S"},
    {"texto": "Frequentemente dedico tempo imaginando cenários futuros e possibilidades teóricas.", "traco": "N"},
    {"texto": "Tenho preferência por instruções metodológicas e detalhadas em vez de conceitos amplos.", "traco": "S"},
    {"texto": "Sinto motivação em buscar padrões ocultos e conexões subjacentes entre informações diversas.", "traco": "N"},
    {"texto": "Possuo alta percepção do ambiente imediato e noto detalhes factuais com facilidade.", "traco": "S"},
    {"texto": "Questiono constantemente os motivos fundamentais em vez de aceitar o estado atual das coisas.", "traco": "N"},
    {"texto": "Valorizo soluções pragmáticas que apresentam aplicabilidade imediata e comprovada.", "traco": "S"},
    {"texto": "Aprecio debates sobre ideias conceituais ou filosóficas, independentemente de sua utilidade prática.", "traco": "N"},

    {"texto": "Considero a lógica objetiva mais relevante do que o impacto emocional das decisões.", "traco": "T"},
    {"texto": "Avalio o impacto interpessoal e o bem-estar coletivo como fatores centrais em minhas escolhas.", "traco": "F"},
    {"texto": "Em um debate acadêmico ou profissional, meu foco é a precisão dos fatos, não a harmonia.", "traco": "T"},
    {"texto": "Apresento alta empatia, frequentemente internalizando o estado emocional das pessoas ao meu redor.", "traco": "F"},
    {"texto": "Prefiro atuar com lideranças diretas e focadas em eficiência, mesmo que pareçam ríspidas.", "traco": "T"},
    {"texto": "Acredito que a consideração humana e a flexibilidade superam a aplicação estrita de regras.", "traco": "F"},
    {"texto": "Diante do problema de um colega, ofereço planos de ação e soluções antes de suporte emocional.", "traco": "T"},
    {"texto": "Causar desconforto a terceiros me afeta significativamente, mesmo quando minha posição está correta.", "traco": "F"},

    {"texto": "Mantenho um alto nível de planejamento estruturado para minhas atividades rotineiras.", "traco": "J"},
    {"texto": "Prefiro manter um grau de flexibilidade e adaptar minhas decisões conforme o cenário evolui.", "traco": "P"},
    {"texto": "A falta de organização prévia ou ambientes caóticos geram desconforto significativo para mim.", "traco": "J"},
    {"texto": "Demonstro alta resiliência e adaptabilidade diante de mudanças repentinas de escopo.", "traco": "P"},
    {"texto": "Priorizo estritamente a conclusão de responsabilidades antes de momentos de lazer.", "traco": "J"},
    {"texto": "Apresento picos de produtividade quando submetido à pressão de prazos iminentes.", "traco": "P"},
    {"texto": "Utilizo ferramentas de gestão (cronogramas, listas) de forma contínua para guiar meu dia.", "traco": "J"},
    {"texto": "Estruturas processuais excessivamente rígidas tendem a limitar meu potencial criativo.", "traco": "P"}
]

DESCRICOES_PERFIS = {
    "INTJ": {
        "titulo": "O Estrategista",
        "resumo": "Pensadores criativos e estratégicos, com um plano de longo prazo para todas as situações.",
        "comportamento": "Enxergam o mundo como um sistema complexo a ser otimizado. Valorizam a competência técnica, a racionalidade e a independência. Podem parecer distantes ou excessivamente críticos devido à sua constante análise interna. Detestam ineficiência, redundância e regras sem fundamentação lógica.",
        "como_agir": "Seja objetivo, estruturado e fundamente seus argumentos em lógica e dados empíricos. Evite apelos puramente emocionais ou dramatizações. Conceda autonomia e tempo para que processem informações complexas isoladamente. Comunique o objetivo final antes dos detalhes."
    },
    "INTP": {
        "titulo": "O Lógico",
        "resumo": "Inovadores intelectuais com uma sede insaciável por conhecimento e análise de sistemas.",
        "comportamento": "Operam movidos pela curiosidade e pelo desejo de compreender o funcionamento das coisas. São adaptáveis em pensamento, mas rigorosos na lógica. Frequentemente se perdem em teorias e podem negligenciar a execução prática ou dinâmicas sociais superficiais.",
        "como_agir": "Estimule o intelecto promovendo debates construtivos. Não exija adesão cega a protocolos; explique a razão subjacente. Evite pressioná-los por decisões emocionais rápidas e valorize sua capacidade de encontrar inconsistências."
    },
    "ENTJ": {
        "titulo": "O Comandante",
        "resumo": "Líderes natos, assertivos e focados em estruturar o ambiente para alcançar resultados eficientes.",
        "comportamento": "Assumem o controle das situações naturalmente. Focam na macrogestão, metas de longo prazo e resolução rápida de obstáculos. Possuem pouca tolerância para incompetência ou desorganização, podendo demonstrar impaciência com ritmos de trabalho mais lentos.",
        "como_agir": "Demonstre confiança e competência. Comunique-se de forma direta, clara e orientada a soluções e resultados operacionais. Não tome o estilo incisivo deles como ataque pessoal. Esteja preparado para defender suas ideias com argumentos sólidos."
    },
    "ENTP": {
        "titulo": "O Inovador",
        "resumo": "Pensadores ágeis e argumentativos que enxergam possibilidades contínuas e adoram desafios intelectuais.",
        "comportamento": "Processam informações verbalmente através de debates. São adeptos de encontrar novas abordagens e frequentemente atuam como 'advogados do diabo'. Tendem a perder o interesse após a fase de ideação, delegando a manutenção e a rotina.",
        "como_agir": "Mantenha a mente aberta e esteja disposto a sessões de brainstorming não lineares. Evite o microgerenciamento ou a imposição de rotinas estritas. Ao debater, foque no mérito intelectual das ideias, compreendendo que a argumentação é o método de processamento deles."
    },
    "INFJ": {
        "titulo": "O Conselheiro",
        "resumo": "Idealistas reservados e visionários, motivados por valores profundos e conexões autênticas.",
        "comportamento": "Agem com propósito e foco no bem-estar humano de longo prazo. São altamente empáticos, mas preservam uma natureza privada. Preferem atuar nos bastidores para promover mudanças estruturais e éticas, evitando conflitos superficiais.",
        "como_agir": "Comunique-se com autenticidade e transparência. Respeite sua necessidade de privacidade e períodos de isolamento. Alinhe propostas aos seus valores éticos e forneça um ambiente de confiança, evitando táticas de manipulação ou agressividade corporativa."
    },
    "INFP": {
        "titulo": "O Mediador",
        "resumo": "Indivíduos poéticos e altruístas, guiados por um forte núcleo de valores morais e pessoais.",
        "comportamento": "Priorizam a autenticidade e a harmonia interna. São flexíveis e de mente aberta, exceto quando seus valores fundamentais são violados. Possuem uma rica vida interior e criatividade aguçada, mas podem ter dificuldade com tarefas puramente burocráticas.",
        "como_agir": "Valide suas emoções e demonstre empatia. Forneça críticas de forma construtiva e gentil, pois tendem a internalizar feedbacks negativos. Engaje-os através de causas, propósitos e impactos positivos na vida das pessoas."
    },
    "ENFJ": {
        "titulo": "O Protagonista",
        "resumo": "Líderes carismáticos e empáticos, focados em desenvolver o potencial humano ao seu redor.",
        "comportamento": "Possuem excelente leitura social e facilidade em unir grupos em prol de objetivos comuns. Sentem responsabilidade pelo clima emocional do ambiente. Podem negligenciar as próprias necessidades ao tentar resolver os problemas de toda a equipe.",
        "como_agir": "Reconheça e agradeça o esforço que investem nas relações interpessoais. Trabalhe de forma colaborativa e demonstre consideração pelo impacto humano das decisões. Evite atitudes friamente calculistas que ignorem a moral da equipe."
    },
    "ENFP": {
        "titulo": "O Ativista",
        "resumo": "Espíritos livres, altamente comunicativos, que buscam explorar ideias e significados profundos.",
        "comportamento": "Apresentam energia contagiante e operam bem em ambientes dinâmicos e inovadores. Conectam-se facilmente com diferentes perfis. Sofrem queda drástica de produtividade se submetidos a ambientes altamente regulados, monótonos ou restritivos.",
        "como_agir": "Incentive a expressão criativa e demonstre entusiasmo por suas iniciativas. Forneça diretrizes gerais em vez de regras restritas passo a passo. Mantenha o ambiente flexível e estimulante, reconhecendo suas contribuições inovadoras."
    },
    "ISTJ": {
        "titulo": "O Logístico",
        "resumo": "Indivíduos organizados, responsáveis e rigorosos com processos e cumprimento de deveres.",
        "comportamento": "Operam baseados em fatos concretos e metodologias estabelecidas. São altamente confiáveis para a manutenção de sistemas institucionais. Valorizam a estabilidade, a pontualidade e a clareza, evitando riscos desnecessários ou improvisações não calculadas.",
        "como_agir": "Forneça instruções claras, preferencialmente por escrito, com prazos e expectativas definidas. Honre os compromissos estabelecidos e respeite a hierarquia e os procedimentos. Evite mudanças repentinas e injustificadas de planejamento."
    },
    "ISFJ": {
        "titulo": "O Defensor",
        "resumo": "Colaboradores dedicados e protetores, focados em manter a estabilidade e o suporte prático da equipe.",
        "comportamento": "Atuam de forma meticulosa para garantir que as necessidades práticas e diárias das pessoas sejam atendidas. São leais e possuem excelente memória para detalhes. Evitam confrontos diretos e muitas vezes hesitam em assumir os créditos por seu trabalho árduo.",
        "como_agir": "Demonstre gratidão explícita por suas contribuições, que frequentemente ocorrem nos bastidores. Mantenha um ambiente estruturado e previsível. Ao introduzir mudanças, faça-o de forma gradual, explicando como isso beneficiará a estabilidade do grupo."
    },
    "ESTJ": {
        "titulo": "O Executivo",
        "resumo": "Administradores práticos e tradicionais, inigualáveis no gerenciamento eficiente de processos ou pessoas.",
        "comportamento": "Tendem a padronizar procedimentos e delegar tarefas com clareza. Possuem foco voltado para a métrica, a ordem e a conformidade com regras institucionais. Podem ser inflexíveis com opiniões que contrariem procedimentos já validados empiricamente.",
        "como_agir": "Seja pontual, direto e comprove a eficácia de suas propostas com dados e métricas reais. Respeite as estruturas de autoridade estabelecidas. Não apresente problemas sem ao menos sugerir uma solução estruturada em etapas."
    },
    "ESFJ": {
        "titulo": "O Cônsul",
        "resumo": "Indivíduos sociais, atentos aos detalhes e focados em promover o bem-estar e a integração do grupo.",
        "comportamento": "São motivados pelo desejo de serem úteis e manter a ordem social. Organizam eventos e cuidam da logística humana de qualquer projeto. Buscam validação externa constante e evitam ambientes competitivos, preferindo a colaboração mútua.",
        "como_agir": "Fomente um ambiente cordial e demonstre interesse genuíno por seu bem-estar. Reconheça seus esforços abertamente. Ao discutir problemas organizacionais, foque em como restaurar a harmonia e a cooperação entre os membros da equipe."
    },
    "ISTP": {
        "titulo": "O Virtuoso",
        "resumo": "Experimentadores práticos e analíticos, com notável habilidade para solucionar problemas imediatos.",
        "comportamento": "Observam o ambiente em silêncio até que uma ação seja necessária. Aprendem manipulando variáveis e lidam excepcionalmente bem com crises. Não apreciam teorias excessivamente abstratas e possuem baixa tolerância para protocolos que consideram irrelevantes.",
        "como_agir": "Vá direto à questão prática. Evite reuniões teóricas prolongadas e excesso de formalidade. Conceda autonomia técnica e espaço físico. Ao solicitar ajuda, apresente o problema como um desafio tangível a ser resolvido."
    },
    "ISFP": {
        "titulo": "O Aventureiro",
        "resumo": "Artistas observadores, flexíveis e sensíveis às nuances estéticas e emocionais do ambiente.",
        "comportamento": "Vivem ancorados no momento presente e buscam a harmonia ambiental. São amigáveis, não-julgadores e evitam a tentativa de controlar terceiros. Necessitam de espaço pessoal e costumam demonstrar afeto e lealdade através de ações práticas, não de palavras.",
        "como_agir": "Comunique-se com suavidade e sem agressividade competitiva. Não os pressione a assumir posições de liderança autoritária ou projetar planos de longo prazo com rigidez absoluta. Valorize a qualidade e a estética do trabalho que executam."
    },
    "ESTP": {
        "titulo": "O Empreendedor",
        "resumo": "Indivíduos pragmáticos, focados em ação rápida, percepção de oportunidades e resultados imediatos.",
        "comportamento": "São altamente adaptáveis e prosperam em ambientes de risco calculado ou de constante mudança. Detestam a estagnação e o planejamento excessivo. Leem o ambiente e as pessoas com precisão milimétrica, utilizando essa percepção para negociação.",
        "como_agir": "Mantenha a comunicação rápida, interativa e voltada para a execução imediata. Evite discursos teóricos. Desafie-os com problemas complexos de curto prazo que exijam agilidade mental e intervenção direta no cenário."
    },
    "ESFP": {
        "titulo": "O Animador",
        "resumo": "Pessoas dinâmicas e sociáveis, com notável capacidade de motivar e engajar grupos na execução.",
        "comportamento": "São o centro energético do ambiente. Focam no impacto imediato e possuem forte senso estético e prático. Preferem lidar com pessoas e situações concretas. Podem demonstrar frustração com análises estatísticas isoladas ou planejamento de longo prazo rigoroso.",
        "como_agir": "Mantenha interações otimistas, objetivas e dinâmicas. Evite prendê-los em trabalhos excessivamente solitários ou analíticos. Engaje-os em atividades que exijam relacionamento interpessoal, apresentação de ideias e resposta rápida do público."
    }
}