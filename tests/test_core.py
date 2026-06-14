from types import SimpleNamespace
from unittest.mock import Mock, patch

import pytest

from core import MedTimeCore


def criar_core_com_banco_falso(db_falso):
    with patch("core.obter_conexao", return_value=db_falso):
        return MedTimeCore()


def test_adicionar_medicamento_campos_vazios():
    db_falso = Mock()
    core = criar_core_com_banco_falso(db_falso)

    with pytest.raises(ValueError, match="Todos os campos são obrigatórios."):
        core.adicionar_medicamento("", "08:00", "1 comprimido")


def test_adicionar_medicamento_horario_invalido():
    db_falso = Mock()
    core = criar_core_com_banco_falso(db_falso)

    with pytest.raises(ValueError, match="O horário deve estar no formato HH:MM"):
        core.adicionar_medicamento("Paracetamol", "8h", "1 comprimido")


def test_adicionar_medicamento_com_dados_validos():
    db_falso = Mock()
    tabela_falsa = Mock()

    medicamento_criado = {
        "id": 1,
        "nome": "Paracetamol",
        "horario": "08:00",
        "dosagem": "1 comprimido",
    }

    tabela_falsa.insert.return_value.execute.return_value = SimpleNamespace(
        data=[medicamento_criado]
    )
    db_falso.table.return_value = tabela_falsa

    core = criar_core_com_banco_falso(db_falso)

    resultado = core.adicionar_medicamento(
        "Paracetamol",
        "08:00",
        "1 comprimido",
    )

    assert resultado == medicamento_criado
    db_falso.table.assert_called_once_with("medicamentos")
    tabela_falsa.insert.assert_called_once_with(
        {
            "nome": "Paracetamol",
            "horario": "08:00",
            "dosagem": "1 comprimido",
        }
    )


def test_remover_medicamento_id_inexistente():
    db_falso = Mock()
    tabela_falsa = Mock()
    delete_falso = Mock()
    eq_falso = Mock()

    eq_falso.execute.return_value = SimpleNamespace(data=[])
    delete_falso.eq.return_value = eq_falso
    tabela_falsa.delete.return_value = delete_falso
    db_falso.table.return_value = tabela_falsa

    core = criar_core_com_banco_falso(db_falso)

    resultado = core.remover_medicamento(999999)

    assert resultado is False
    db_falso.table.assert_called_once_with("medicamentos")
    tabela_falsa.delete.assert_called_once()
    delete_falso.eq.assert_called_once_with("id", 999999)
