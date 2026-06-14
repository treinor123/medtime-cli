import sys

from tabulate import tabulate

from core import MedTimeCore


def exibir_menu():
    print("\n========================================")
    print("      MEDTIME - CONTROLE DE REMÉDIOS      ")
    print("========================================")
    print("1. Cadastrar Novo Medicamento")
    print("2. Listar Meus Medicamentos")
    print("3. Remover Medicamento")
    print("4. Sair")
    print("========================================")


def main():
    core = MedTimeCore()

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (1-4): ").strip()

        if opcao == "1":
            print("\n--- CADASTRAR REMÉDIO ---")
            nome = input("Nome do Medicamento: ")
            horario = input("Horário (ex: 08:00): ")
            dosagem = input("Dosagem (ex: 1 comprimido, 5ml): ")

            try:
                core.adicionar_medicamento(nome, horario, dosagem)
                print("\n✅ Cadastrado com sucesso no banco em nuvem!")
            except ValueError as e:
                print(f"\n❌ Erro: {e}")

        elif opcao == "2":
            print("\n--- SEUS MEDICAMENTOS ---")
            lista = core.listar_medicamentos()

            if not lista:
                print("Nenhum medicamento agendado ainda.")
            else:
                dados = [
                    [m["id"], m["nome"], m["horario"], m["dosagem"]]
                    for m in lista
                ]

                print(
                    tabulate(
                        dados,
                        headers=["ID", "Nome", "Horário", "Dosagem"],
                        tablefmt="grid",
                    )
                )

        elif opcao == "3":
            print("\n--- REMOVER REMÉDIO ---")

            try:
                med_id = int(input("Digite o ID do medicamento para remover: "))

                if core.remover_medicamento(med_id):
                    print("\n✅ Medicamento removido do banco com sucesso!")
                else:
                    print("\n❌ ID não encontrado no banco de dados.")
            except ValueError:
                print("\n❌ Por favor, digite um ID numérico válido.")

        elif opcao == "4":
            print("\nObrigado por usar o MedTime! Cuide da sua saúde. 👋")
            sys.exit(0)

        else:
            print("\n❌ Opção inválida. Escolha um número de 1 a 4.")


if __name__ == "__main__":
    main()
