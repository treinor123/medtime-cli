from database import obter_conexao


class MedTimeCore:
    def __init__(self):
        self.db = obter_conexao()

    def listar_medicamentos(self) -> list:
        """Busca todos os medicamentos diretamente do banco de dados Supabase."""
        try:
            resposta = (
                self.db.table("medicamentos")
                .select("*")
                .order("horario")
                .execute()
            )
            return resposta.data
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return []

    def adicionar_medicamento(self, nome: str, horario: str, dosagem: str) -> dict:
        """Valida os dados e insere um novo medicamento no Supabase."""
        if not nome.strip() or not horario.strip() or not dosagem.strip():
            raise ValueError("Todos os campos são obrigatórios.")

        if len(horario) != 5 or horario[2] != ":":
            raise ValueError("O horário deve estar no formato HH:MM (ex: 08:00).")

        novo_med = {
            "nome": nome.strip(),
            "horario": horario.strip(),
            "dosagem": dosagem.strip(),
        }

        resposta = self.db.table("medicamentos").insert(novo_med).execute()
        return resposta.data[0]

    def remover_medicamento(self, med_id: int) -> bool:
        """Remove um medicamento do Supabase usando o ID."""
        resposta = (
            self.db.table("medicamentos")
            .delete()
            .eq("id", med_id)
            .execute()
        )
        return len(resposta.data) > 0
