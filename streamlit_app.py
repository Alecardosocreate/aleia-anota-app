import streamlit as st
import pandas as pd
from datetime import datetime

# 1. Configuração da página
st.set_page_config(
    page_title="Aleia Anota",
    page_icon="🤖",
    layout="centered"
)

# 2. Cabeçalho
st.title("Oi! Sou a Aleia Anota 🤖")
st.markdown("### Assistente virtual da Ale para demandas de UX/UI")

# --- Criando Abas para separar o Pedido da Visualização ---
aba_pedido, aba_fila = st.tabs(["📝 Fazer Solicitação", "👀 Ver Fila & Status"])

# ==========================================
# ABA 1: O FORMULÁRIO
# ==========================================
with aba_pedido:
    st.info("Preencha os dados abaixo para eu organizar a fila da Ale!")
    
    with st.form("my_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            nome = st.text_input("Seu Nome")
            area = st.selectbox(
                "Sua Área", 
                ["Analista de Requisitos", "Scrum Master", "Desenvolvimento", "Outro"]
            )
            projeto = st.text_input("Qual Projeto?")
            
        with col2:
            demanda_opcoes = [
                "Nova Tela (Design System Gov.br)",
                "Opinião de Ux/Ui",
                "Jornada do Usuário",
                "Sustentação (Legado)",
                "Problemas no figma",
                "Ajustes de protótipo/ Bug Visual",
                "Melhorias em telas ja feitas",
                "Outro (Escrever)"
            ]
            
            demanda_selecionada = st.selectbox("O que você precisa?", demanda_opcoes)
            
            demanda_final = demanda_selecionada
            if demanda_selecionada == "Outro (Escrever)":
                demanda_final = st.text_input("Descreva o tipo de demanda:")
            
            prioridade = st.select_slider(
                "Prioridade", 
                options=["Baixa", "Média", "Alta", "Pra ontem 🔥"]
            )

        descricao = st.text_area("Descreva o que precisa (pode colar links aqui)")
        
        # Campo de Upload
        arquivo = st.file_uploader("Anexar print, doc ou rascunho (opcional)", type=['png', 'jpg', 'pdf', 'docx'])

        # Botão de Envio
        submitted = st.form_submit_button("Enviar Solicitação ✨")

        if submitted:
            if not nome or not projeto:
                st.warning("Opa! Nome e Projeto são obrigatórios.")
            else:
                st.success(f"Recebido, {nome}! A Ale vai analisar o pedido do projeto **{projeto}**.")
                st.balloons()
    
    st.divider()
    
    st.markdown("### Vamos conversar?")
    
    # SEU E-MAIL
try:
        meu_email_mma = st.secrets["email_mma"]
except FileNotFoundError:
        st.error("Configure o secrets.toml para o botão funcionar!")
        meu_email_mma = "erro@configuracao.com"

col_ag1 = st.columns(1)[0] # O [0] pega a primeira coluna da lista

with col_ag1:
        # Link que abre direto o chat do Teams com você
        link_teams = f"https://teams.microsoft.com/l/chat/0/0?users={meu_email_mma}"
        st.link_button("💬 Chamar no Chat (Teams)", link_teams)

# ==========================================
# ABA 2: A FILA (DASHBOARD)
# ==========================================
with aba_fila:
    st.markdown("### Fila de Prioridades da Ale")
    st.caption("Acompanhe aqui o status do seu pedido.")

    # --- DADOS MOCKADOS (DE MENTIRINHA) PARA VISUALIZAÇÃO ---
    # Como ainda não ligamos num banco de dados, criei essa lista fixa 
    # só pra você ver como vai ficar o layout.
    dados_exemplo = [
        {"Data": "15/01", "Solicitante": "Carlos (Dev)", "Projeto": "App Mobile", "Demanda": "Tela Login", "Prioridade": "Alta", "Status": "🏃‍♀️ Em Andamento"},
        {"Data": "16/01", "Solicitante": "Mari (PO)", "Projeto": "Portal RH", "Demanda": "Ajuste Botão", "Prioridade": "Baixa", "Status": "✅ Concluído"},
        {"Data": "16/01", "Solicitante": "Você", "Projeto": "Novo Sistema", "Demanda": "Wireframe", "Prioridade": "Média", "Status": "⏳ Na Fila"},
    ]
    
    # Criando a Tabela Visual
    df = pd.DataFrame(dados_exemplo)
    
    # Mostrando a tabela com estilo
    st.dataframe(
        df, 
        use_container_width=True,
        hide_index=True,
        column_config={
            "Status": st.column_config.SelectboxColumn(
                "Status",
                help="Status atual da demanda",
                width="medium",
                options=["⏳ Na Fila", "🏃‍♀️ Em Andamento", "🎨 Em Review", "✅ Concluído"],
            )
        }
    )