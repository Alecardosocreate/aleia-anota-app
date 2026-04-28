import streamlit as st
import pandas as pd
from datetime import datetime
from streamlit_gsheets import GSheetsConnection

# 1. Configuração da página
st.set_page_config(
    page_title="Aleia Anota",
    page_icon="🤖",
    layout="centered"
)

# 2. Conexão com Google Sheets (Tenta ler os dados)
try:
    conn = st.connection("gsheets", type=GSheetsConnection)
    existing_data = conn.read(worksheet="Página1", usecols=list(range(8)), ttl=5)
    existing_data = existing_data.dropna(how="all")
except Exception as e:
    # Se falhar ou não tiver planilha configurada ainda, cria uma tabela vazia
    existing_data = pd.DataFrame(columns=["Data", "Nome", "Area", "Projeto", "Demanda", "Prioridade", "Descricao", "Status"])

# 3. Cabeçalho
st.title("Oi! Sou a Aleia Anota 🤖")
st.markdown("### Assistente virtual da Ale para demandas de UX/UI")

aba_pedido, aba_fila = st.tabs(["📝 Fazer Solicitação", "👀 Ver Fila & Status"])

# ==========================================
# ABA 1: O FORMULÁRIO INTELIGENTE
# ==========================================
with aba_pedido:
    st.info("Preencha os dados abaixo para eu organizar a fila da Ale!")
    
    with st.form("my_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            nome = st.text_input("Seu Nome")
            
            # Lógica para Área + Campo "Outro"
            area_opcoes = ["Analista de Requisitos", "Scrum Master", "Desenvolvimento", "Outro (Escrever)"]
            area_selecionada = st.selectbox("Sua Área", area_opcoes)
            
            area_final = area_selecionada
            if area_selecionada == "Outro (Escrever)":
                area_final = st.text_input("Digite qual sua área:")

            projeto = st.text_input("Qual Projeto?")
            
        with col2:
            # Lógica para Demanda + Campo "Outro"
            demanda_opcoes = [
                "Nova Tela (Design System Gov.br)",
                "Opinião de Ux/Ui",
                "Jornada do Usuário",
                "Sustentação (Legado)",
                "Problemas no Figma",
                "Ajustes de protótipo/ Bug Visual",
                "Melhorias em telas já feitas",
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
        arquivo = st.file_uploader("Anexar print, doc ou rascunho", type=['png', 'jpg', 'pdf', 'docx'])

        submitted = st.form_submit_button("Enviar Solicitação ✨")

        if submitted:
            if not nome or not projeto or not descricao:
                st.warning("Preencha Nome, Projeto e Descrição para enviar.")
            else:
                # Se tivesse a planilha conectada, salvaria aqui. 
                # Por enquanto apenas mostra o sucesso na tela.
                st.success(f"Recebido! O pedido sobre **{demanda_final}** já está na fila.")
                st.balloons()

    st.divider()
    
    # Seção de Contato
    st.markdown("### Vamos conversar?")
    
    # Link protegido (depois configuramos o secrets.toml com o seu email real)
    try:
        meu_email_mma = st.secrets["email_mma"]
    except:
        meu_email_mma = "seu.email@mma.gov.br"

    link_teams = f"https://teams.microsoft.com/l/chat/0/0?users={meu_email_mma}"
    st.link_button("💬 Chamar no Chat (Teams)", link_teams, use_container_width=True)

# ==========================================
# ABA 2: A FILA EM TEMPO REAL
# ==========================================
with aba_fila:
    st.markdown("### Fila de Prioridades da Ale")
    
    if st.button("🔄 Atualizar Fila"):
        st.cache_data.clear()
        st.rerun()

    st.dataframe(
        existing_data, 
        use_container_width=True,
        hide_index=True,
        column_order=["Data", "Nome", "Projeto", "Demanda", "Prioridade", "Status"],
        column_config={
            "Status": st.column_config.TextColumn(
                "Status",
                help="Status atual da demanda",
                width="medium"
            )
        }
    )