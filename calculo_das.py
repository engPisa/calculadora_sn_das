def calcular_das_completo(anexo, faturamento, rbt12):
    """Calcula DAS, determinando a faixa e a distribuicao especifica."""
    import json
    from tabelas import tabelas_simples

    with open("distribuicao_impostos.json", "r", encoding="utf-8") as f:
        distribuicao = json.load(f)

    tabela = tabelas_simples[anexo]
    faixa_num = None
    for idx, faixa in enumerate(tabela, start=1):
        if rbt12 <= faixa["limite"]:
            aliquota = faixa["aliquota"] / 100
            deducao = faixa["deducao"]
            faixa_num = str(idx)
            break

    aliq_efetiva = ((faturamento * aliquota) - deducao) / faturamento
    das = faturamento * aliq_efetiva

    partilha = distribuicao[anexo][faixa_num]
    dist = {imp: round(das * perc, 2) for imp, perc in partilha.items()}

    return aliq_efetiva, das, dist


def calcular_totais_contabeis(das, distribuicao, iss_retido):
    iss_distribuido = distribuicao.get("ISS", 0)
    iss_final = iss_retido
    das_sem_iss = das - iss_distribuido
    total_pago = das_sem_iss + iss_final

    return {
        "das_total": round(das, 2),
        "iss_distribuido": round(iss_distribuido, 2),
        "iss_retido": round(iss_retido, 2),
        "das_sem_iss": round(das_sem_iss, 2),
        "total_contabil": round(total_pago, 2)
    }
