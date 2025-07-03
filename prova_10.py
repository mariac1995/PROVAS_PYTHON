import streamlit as st

# Configuração da página
st.set_page_config(page_title="Formulário de Contato", layout="centered")

# Título
st.title("Formulário de Contato")

# Espaço entre elementos
st.write("Por favor, preencha os campos abaixo e clique em *Enviar*.")

# Formulário
with st.form(key="formulario_contato"):
    nome = st.text_input("Nome")
    email = st.text_input("Email")
    mensagem = st.text_area("Mensagem")

    enviar = st.form_submit_button("Enviar")

    if enviar:
        if nome.strip() == "" or email.strip() == "" or mensagem.strip() == "":
            st.warning("Por favor, preencha todos os campos antes de enviar.")
        else:
            # Aqui você pode processar os dados, salvar em banco, enviar e-mail, etc.
            st.success(f"Obrigado, {nome}! Sua mensagem foi enviada com sucesso.")