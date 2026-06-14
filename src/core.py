from database import obter_conexao

class MedTimeCore:
    def _init_(self):
        # Aqui pegamos a conexão que o Integrante 1 configurou
        self.db = obter_conexao()

    def listar_medicamentos(self) -> list:
        """Busca todos os medicamentos diretamente do banco de dados Supabase."""
        try:
            # Faz um 'SELECT *' na tabela ordenar por horário
            resposta = self.db.table("medicamentos").select("*").order("horario").execute()
            return resposta.data
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return []