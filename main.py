import tkinter as tk
from tkinter import messagebox
import os
from dados import PERGUNTAS
from motor_calculo import calcular_perfil
from gerador_relatorio import gerar_relatorio_html

class AvaliacaoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Avaliação Psicométrica")
        self.root.geometry("850x550")
        self.root.configure(bg="#f8fafc")
        self.root.resizable(False, False)

        self.respostas = []
        self.pergunta_atual = 0
        self.nome = ""

        # Configuração de Fontes e Cores
        self.f_titulo = ("Segoe UI", 24, "bold")
        self.f_sub = ("Segoe UI", 12)
        self.f_pergunta = ("Segoe UI", 16, "bold")
        self.f_btn = ("Segoe UI", 11, "bold")
        
        self.cor_fundo = "#f8fafc"
        self.cor_texto = "#0f172a"
        
        # Frame principal que vai conter as telas
        self.container = tk.Frame(root, bg=self.cor_fundo)
        self.container.pack(expand=True, fill="both", padx=40, pady=40)

        self.tela_inicial()

    def limpar_tela(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    def tela_inicial(self):
        self.limpar_tela()

        # Título
        tk.Label(self.container, text="Avaliação Psicométrica Corporativa", 
                 font=self.f_titulo, bg=self.cor_fundo, fg=self.cor_texto).pack(pady=(40, 10))
        
        tk.Label(self.container, text="Descubra seu arquétipo, traços dominantes e estilo operacional.", 
                 font=self.f_sub, bg=self.cor_fundo, fg="#64748b").pack(pady=(0, 40))

        # Campo de Nome
        tk.Label(self.container, text="Digite seu nome completo:", 
                 font=("Segoe UI", 12, "bold"), bg=self.cor_fundo, fg=self.cor_texto).pack(pady=(10, 5))
        
        self.entry_nome = tk.Entry(self.container, font=("Segoe UI", 14), width=40, 
                                   bg="#ffffff", fg="#0f172a", relief="solid", borderwidth=1)
        self.entry_nome.pack(pady=10, ipady=8)

        # Botão Iniciar
        btn_iniciar = tk.Button(self.container, text="INICIAR AVALIAÇÃO", font=self.f_btn, 
                                bg="#0284c7", fg="#ffffff", activebackground="#0369a1", activeforeground="white",
                                relief="flat", cursor="hand2", command=self.iniciar_teste)
        btn_iniciar.pack(pady=30, ipadx=30, ipady=12)

    def iniciar_teste(self):
        nome_input = self.entry_nome.get().strip()
        if not nome_input:
            messagebox.showwarning("Aviso", "Por favor, insira o seu nome para continuar.")
            return
        
        self.nome = nome_input
        self.pergunta_atual = 0
        self.respostas = []
        self.tela_pergunta()

    def registrar_resposta(self, valor):
        self.respostas.append(valor)
        self.pergunta_atual += 1
        
        if self.pergunta_atual < len(PERGUNTAS):
            self.tela_pergunta()
        else:
            self.finalizar_teste()

    def tela_pergunta(self):
        self.limpar_tela()
        
        total = len(PERGUNTAS)
        p_atual = self.pergunta_atual + 1
        pergunta_texto = PERGUNTAS[self.pergunta_atual]["texto"]

        # Barra de progresso (texto)
        tk.Label(self.container, text=f"PERGUNTA {p_atual} DE {total}", 
                 font=("Segoe UI", 10, "bold"), bg=self.cor_fundo, fg="#94a3b8").pack(pady=(20, 10))

        # Texto da Pergunta
        lbl_pergunta = tk.Label(self.container, text=pergunta_texto, font=self.f_pergunta, 
                                bg=self.cor_fundo, fg=self.cor_texto, wraplength=700, justify="center")
        lbl_pergunta.pack(pady=(20, 50), fill="x")

        # Frame para os botões alinhados horizontalmente
        frame_botoes = tk.Frame(self.container, bg=self.cor_fundo)
        frame_botoes.pack(pady=20)

        # Configuração visual dos 5 botões (Cores variando do Vermelho ao Verde)
        opcoes = [
            (1, "Discordo\nTotalmente", "#ef4444", "#dc2626"), # Vermelho
            (2, "Discordo\nParcialmente", "#f97316", "#ea580c"), # Laranja
            (3, "Posição\nNeutra", "#94a3b8", "#64748b"), # Cinza
            (4, "Concordo\nParcialmente", "#84cc16", "#65a30d"), # Verde claro
            (5, "Concordo\nTotalmente", "#22c55e", "#16a34a")  # Verde escuro
        ]

        for valor, texto, cor_bg, cor_hover in opcoes:
            btn = tk.Button(frame_botoes, text=texto, font=("Segoe UI", 10, "bold"),
                            bg=cor_bg, fg="#ffffff", activebackground=cor_hover, activeforeground="white",
                            relief="flat", cursor="hand2", width=14, height=3,
                            command=lambda v=valor: self.registrar_resposta(v))
            btn.pack(side="left", padx=8)

    def finalizar_teste(self):
        self.limpar_tela()
        
        tk.Label(self.container, text="Analisando Perfil...", font=self.f_titulo, 
                 bg=self.cor_fundo, fg=self.cor_texto).pack(pady=(120, 20))
        
        tk.Label(self.container, text="Gerando dashboard psicométrico e salvando relatório.", 
                 font=self.f_sub, bg=self.cor_fundo, fg="#64748b").pack()

        # Usa o método 'after' para dar tempo da tela atualizar antes de processar
        self.root.after(1000, self.processar_resultados)

    def processar_resultados(self):
        # 1. Realiza o cálculo (motor)
        perfil, dados_perfil, metricas, status_unico = calcular_perfil(self.respostas)
        
        # 2. Gera o relatório (gerador visual)
        arquivo_saida = f"relatorio_{self.nome.replace(' ', '_').lower()}.html"
        gerar_relatorio_html(self.nome, perfil, dados_perfil, metricas, status_unico, arquivo_saida)
        
        # 3. Atualiza a tela informando sucesso
        self.limpar_tela()
        tk.Label(self.container, text="Relatório Gerado com Sucesso!", font=self.f_titulo, 
                 bg=self.cor_fundo, fg="#22c55e").pack(pady=(100, 20))
        
        tk.Label(self.container, text=f"O arquivo foi salvo como:\n{arquivo_saida}", 
                 font=self.f_sub, bg=self.cor_fundo, fg=self.cor_texto, justify="center").pack(pady=10)
                 
        tk.Label(self.container, text="O relatório foi aberto automaticamente no seu navegador.", 
                 font=("Segoe UI", 10, "italic"), bg=self.cor_fundo, fg="#64748b").pack(pady=20)
        
        btn_sair = tk.Button(self.container, text="FINALIZAR E FECHAR", font=self.f_btn, 
                             bg="#0f172a", fg="#ffffff", activebackground="#334155", activeforeground="white",
                             relief="flat", cursor="hand2", command=self.root.quit)
        btn_sair.pack(pady=40, ipadx=30, ipady=10)

if __name__ == "__main__":
    janela_principal = tk.Tk()
    app = AvaliacaoApp(janela_principal)
    janela_principal.mainloop()