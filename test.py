from calculo_das import calcular_das_completo


def main():
    anexo = "III"
    faturamento = 12000.0
    rbt12 = 100000.0

    aliq, das, distribuicao = calcular_das_completo(anexo, faturamento, rbt12)

    assert isinstance(aliq, float), "A alíquota deve ser um float"
    assert isinstance(das, float), "O DAS deve ser um float"
    assert isinstance(distribuicao, dict), "A distribuição deve ser um dicionário"

    soma_distribuicao = sum(distribuicao.values())
    # pequena diferença permitida devido aos arredondamentos de centavos
    assert abs(soma_distribuicao - round(das, 2)) <= 5, (
        f"Soma da distribuição ({soma_distribuicao}) diverge do DAS calculado ({das})"
    )

    print("Teste concluído com sucesso")


if __name__ == "__main__":
    main()
