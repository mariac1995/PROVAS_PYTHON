import streamlit as st

# Inicializa a lista de tarefas na sessão
if "tarefas" not in st.session_state:
    st.session_state.tarefas = []

# Título da aplicação
st.title("📝 Lista de Tarefas")

# Campo de entrada de texto
nova_tarefa = st.text_input("Digite uma nova tarefa:")

# Botão para adicionar tarefa
if st.button("Adicionar"):
    if nova_tarefa.strip():
        st.session_state.tarefas.append(nova_tarefa.strip())
        st.success(f"Tarefa '{nova_tarefa}' adicionada com sucesso!")
    else:
        st.warning("Digite um nome válido para a tarefa.")

# Exibe a lista de tarefas
st.subheader("Tarefas cadastradas:")
if st.session_state.tarefas:
    for i, tarefa in enumerate(st.session_state.tarefas, start=1):
        st.write(f"{i}. {tarefa}")
else:
    st.info("Nenhuma tarefa cadastrada ainda.")
