import streamlit as st

# Configuração da página
st.set_page_config(page_title="Lista de Tarefas", layout="centered")
st.title("Lista de Tarefas")

# Inicializa a lista de tarefas na sessão
if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

# Formulário para adicionar tarefas
with st.form(key="form_tarefa"):
    nova_tarefa = st.text_input("Digite a tarefa")
    adicionar = st.form_submit_button("Adicionar")

    if adicionar:
        if nova_tarefa.strip() == "":
            st.warning("Por favor, digite uma tarefa válida.")
        else:
            st.session_state.tarefas.append(nova_tarefa)
            st.success(f"Tarefa adicionada: {nova_tarefa}")

# Exibir lista de tarefas
st.subheader("Tarefas adicionadas:")
if st.session_state.tarefas:
    for i, tarefa in enumerate(st.session_state.tarefas, start=1):
        st.write(f"{i}. {tarefa}")
else:
    st.info("Nenhuma tarefa adicionada ainda.")