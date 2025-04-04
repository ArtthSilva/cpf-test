import pytest
from app.validacao import validar_cpf

class TestValidacaoCPF:
    def test_cpf_valido(self):
        print("Testando CPF válido")
        assert validar_cpf("529.982.247-25")
        assert validar_cpf("52998224725")

    def test_cpf_invalido_tamanho_errado(self):
        print("Testando CPF com tamanho errado")
        assert not validar_cpf("123.456.789-0")
        assert not validar_cpf("1234567890")

    def test_cpf_invalido_digito_errado(self):
        print("Testando CPF com dígito verificador errado")
        assert not validar_cpf("529.982.247-26")

    def test_cpf_com_todos_digitos_iguais(self):
        print("Testando CPF com todos os dígitos iguais")
        for i in range(10):
            assert not validar_cpf(str(i) * 11)

    def test_cpf_com_caracteres_invalidos(self):
        print("Testando CPF com caracteres inválidos")
        assert not validar_cpf("abc.def.ghi-jk")
        assert not validar_cpf("111.111.111-1a")

    def test_cpf_com_espacos_em_branco(self):
        print("Testando CPF com espaços em branco")
        assert validar_cpf(" 529.982.247-25 ")
        assert validar_cpf(" 52998224725 ")

    def test_cpf_vazio_ou_none(self):
        print("Testando CPF vazio")
        with pytest.raises(ValueError):
            validar_cpf("")

    def test_cpf_com_caracteres_especiais_misturados(self):
        print("Testando CPF com caracteres especiais misturados")
        assert not validar_cpf("52@.98#.247-2*5")

    def test_cpf_com_mais_de_11_digitos(self):
        print("Testando CPF com mais de 11 dígitos")
        assert not validar_cpf("529.982.247-251")

    def test_cpf_com_pontuacao_incompleta(self):
        print("Testando CPF com pontuação incompleta")
        assert validar_cpf("529982.24725")
