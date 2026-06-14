import streamlit as st

from core import MedTimeCore

st.set_page_config(
    page_title="MedTime",
    page_icon="💊",
    layout="centered",
)


def carregar_core():
    return MedTimeCore()


def exibir_medicamentos(core):
    st.subheader("Meus medicamentos")

    medicamentos = core.listar_medicamentos()

    if not medicamentos:
        st.info("Nenhum medicamento cadastrado ainda.")
        return

    st.dataframe(
        medicamentos,
        use_container_width=True,
        hide_index=True,
    )


def cadastrar_medicamento(core):
    st.subheader("Cadastrar novo medicamento")

    with st.form("form_cadastro"):
        nome = st.text_input("Nome do medicamento")
        horario = st.text_input("Horário", placeholder="Ex: 08:00")
        dosagem = st.text_input("Dosagem", placeholder="Ex: 1 comprimido")

        enviado = st.form_submit_button("Cadastrar")

        if enviado:
            try:
                core.adicionar_medicamento(nome, horario, dosagem)
                st.success("Medicamento cadastrado com sucesso!")
                st.rerun()
            except ValueError as erro:
                st.error(str(erro))
            except Exception as erro:
                st.error(f"Erro ao cadastrar medicamento: {erro}")


def remover_medicamento(core):
    st.subheader("Remover medicamento")

    med_id = st.number_input(
        "Digite o ID do medicamento",
        min_value=1,
        step=1,
    )

    if st.button("Remover"):
        try:
            removido = core.remover_medicamento(int(med_id))

            if removido:
                st.success("Medicamento removido com sucesso!")
                st.rerun()
            else:
                st.warning("ID não encontrado no banco de dados.")
        except Exception as erro:
            st.error(f"Erro ao remover medicamento: {erro}")


def main():
    st.title("💊 MedTime")
    st.write("Sistema simples para controle de medicamentos.")

    core = carregar_core()

    aba_listar, aba_cadastrar, aba_remover = st.tabs(
        [
            "Listar",
            "Cadastrar",
            "Remover",
        ]
    )

    with aba_listar:
        exibir_medicamentos(core)

    with aba_cadastrar:
        cadastrar_medicamento(core)

    with aba_remover:
        remover_medicamento(core)


if __name__ == "__main__":
    main()
