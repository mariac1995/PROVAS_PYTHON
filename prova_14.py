import streamlit as st
from datetime import date
import uuid


# =========================
# Classes (POO)
# =========================
class Cliente:
    def __init__(self, nome, telefone, email):
        self.id = str(uuid.uuid4())
        self.nome = nome
        self.telefone = telefone
        self.email = email


class Quarto:
    def __init__(self, numero, tipo, preco_diaria, disponivel=True):
        self.numero = numero
        self.tipo = tipo
        self.preco_diaria = preco_diaria
        self.disponivel = disponivel


class Reserva:
    def __init__(self, cliente, quarto, check_in, check_out, status="Ativa"):
        self.id = str(uuid.uuid4())
        self.cliente = cliente
        self.quarto = quarto
        self.check_in = check_in
        self.check_out = check_out
        self.status = status

    def calcular_valor_total(self):
        dias = (self.check_out - self.check_in).days
        return dias * self.quarto.preco_diaria

    def formatar_datas(self):
        return self.check_in.strftime("%d/%m/%Y"), self.check_out.strftime("%d/%m/%Y")


class GerenciadorDeReservas:
    def __init__(self):
        self.clientes = []
        self.quartos = []
        self.reservas = []

    def adicionar_cliente(self, nome, telefone, email):
        cliente = Cliente(nome, telefone, email)
        self.clientes.append(cliente)
        return cliente

    def adicionar_quarto(self, numero, tipo, preco_diaria, disponivel=True):
        quarto = Quarto(numero, tipo, preco_diaria, disponivel)
        self.quartos.append(quarto)
        return quarto

    def criar_reserva(self, cliente, quarto, check_in, check_out):
        if check_in >= check_out:
            raise ValueError("Data de check-out deve ser após o check-in.")
        if not quarto.disponivel:
            raise ValueError("Quarto indisponível.")
        reserva = Reserva(cliente, quarto, check_in, check_out)
        self.reservas.append(reserva)
        return reserva

    def cancelar_reserva(self, reserva_id):
        for r in self.reservas:
            if r.id == reserva_id:
                r.status = "Cancelada"
                return True
        return False


# =========================
# Inicialização no Streamlit
# =========================
if "ger" not in st.session_state:
    st.session_state.ger = GerenciadorDeReservas()
    # Dados iniciais
    st.session_state.ger.adicionar_cliente(
        "Maria Silva", "31 99999-0001", "maria@example.com"
    )
    st.session_state.ger.adicionar_cliente(
        "João Pereira", "31 98888-0002", "joao@example.com"
    )
    st.session_state.ger.adicionar_quarto(101, "single", 280.0)
    st.session_state.ger.adicionar_quarto(102, "double", 360.0)
    st.session_state.ger.adicionar_quarto(201, "suite", 620.0)

ger = st.session_state.ger

# =========================
# Interface Streamlit
# =========================
st.title("Refúgio dos Sonhos - Sistema de Reservas")

menu = st.sidebar.radio(
    "Navegação", ["Quartos", "Reservas", "Clientes", "Nova Reserva"]
)

# Tela inicial: lista de quartos
if menu == "Quartos":
    st.header("Lista de Quartos")
    for q in ger.quartos:
        st.write(
            f"Quarto {q.numero} - {q.tipo} - R$ {q.preco_diaria:.2f} - {'Disponível' if q.disponivel else 'Indisponível'}"
        )

# Tela de reservas
elif menu == "Reservas":
    st.header("Reservas Atuais")
    if ger.reservas:
        for r in ger.reservas:
            ci, co = r.formatar_datas()
            valor_total = r.calcular_valor_total()
            st.write(
                f"ID: {r.id[:8]} | Cliente: {r.cliente.nome} | Quarto: {r.quarto.numero} | {ci} → {co} | Status: {r.status} | Valor: R$ {valor_total:.2f}"
            )
            if r.status == "Ativa":
                if st.button(f"Cancelar reserva {r.id[:8]}"):
                    ger.cancelar_reserva(r.id)
                    st.success("Reserva cancelada!")
    else:
        st.info("Nenhuma reserva cadastrada.")

# Tela de clientes
elif menu == "Clientes":
    st.header("Clientes cadastrados")
    for c in ger.clientes:
        st.write(f"{c.nome} | Tel: {c.telefone} | Email: {c.email} | ID: {c.id[:8]}")

    st.subheader("Adicionar novo cliente")
    nome = st.text_input("Nome")
    tel = st.text_input("Telefone")
    email = st.text_input("Email")
    if st.button("Cadastrar Cliente"):
        if nome and tel and email:
            ger.adicionar_cliente(nome, tel, email)
            st.success("Cliente cadastrado com sucesso!")
        else:
            st.warning("Preencha todos os campos.")

# Formulário de reserva
elif menu == "Nova Reserva":
    st.header("Criar nova reserva")
    cliente_opcoes = {c.nome: c for c in ger.clientes}
    quarto_opcoes = {f"{q.numero} - {q.tipo}": q for q in ger.quartos if q.disponivel}

    cliente_nome = st.selectbox("Selecione o cliente", list(cliente_opcoes.keys()))
    quarto_nome = st.selectbox("Selecione o quarto", list(quarto_opcoes.keys()))
    check_in = st.date_input("Data de check-in", date.today())
    check_out = st.date_input("Data de check-out", date.today())

    if st.button("Reservar"):
        try:
            cliente = cliente_opcoes[cliente_nome]
            quarto = quarto_opcoes[quarto_nome]
            reserva = ger.criar_reserva(cliente, quarto, check_in, check_out)
            ci, co = reserva.formatar_datas()
            st.success(
                f"Reserva criada com sucesso!\nCheck-in: {ci} | Check-out: {co} | Valor total: R$ {reserva.calcular_valor_total():.2f}"
            )
        except ValueError as e:
            st.error(str(e))
