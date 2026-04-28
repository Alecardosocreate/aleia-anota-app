# 🤖 Aleia Anota - Assistente de Demandas UX/UI

Bem-vindo(a) ao repositório do **Aleia Anota**! Este é um sistema leve de chamados (ticketing) criado para organizar e gerenciar o fluxo de demandas de UX/UI, Requisitos e Desenvolvimento.

Desenvolvido com uma interface "vibe code" e minimalista, o aplicativo permite que os colegas de equipe solicitem tarefas de forma estruturada e acompanhem a fila de prioridades e status em tempo real.

### ✨ Funcionalidades

* **Formulário Inteligente:** Captura de demandas categorizadas (Nova Tela, Ajuste de Fluxo, Review de Design, Bug Visual, etc.).
* **Fila Transparente:** Dashboard em formato de tabela para que toda a equipe veja o que está "Na Fila", "Em Andamento" ou "Concluído".
* **Integração com Google Sheets:** Os dados são salvos e lidos automaticamente de uma planilha na nuvem, servindo como nosso banco de dados.
* **Contato Rápido:** Atalho direto para iniciar um chat no Microsoft Teams ou enviar e-mail.

### 🛠️ Tecnologias Utilizadas

* **[Streamlit](https://streamlit.io/):** Framework principal para construção da interface Web em Python.
* **Pandas:** Para manipulação e exibição dos dados na tabela de fila.
* **Streamlit GSheetsConnection:** Para integração com o Google Sheets.

---

### 🚀 Como executar este projeto na sua máquina

Se você quiser baixar este código e rodar no seu computador, siga os passos abaixo:

1. Clone este repositório e abra a pasta no seu terminal.
2. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt