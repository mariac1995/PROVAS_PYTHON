import streamlit as st

# Título da aplicação
st.title("📩 Formulário de Contato")

# Campos do formulário
nome = st.text_input("Nome")
email = st.text_input("Email")
mensagem = st.text_area("Mensagem")

# Botão de envio
if st.button("Enviar"):
    if nome.strip() and email.strip() and mensagem.strip():
        st.success(
            f"Formulário enviado com sucesso!\n\n"
            f"**Nome:** {nome}\n"
            f"**Email:** {email}\n"
            f"**Mensagem:** {mensagem}"
        )
    else:
        st.warning("⚠️ Por favor, preencha todos os campos antes de enviar.")
