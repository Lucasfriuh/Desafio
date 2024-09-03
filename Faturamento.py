{
    "faturamento": [
        {"dia": 1, "valor": 1000},
        {"dia": 2, "valor": 1500},
        {"dia": 3, "valor": 2000},
        {"dia": 4, "valor": 2500},
        {"dia": 5, "valor": 3000},
        {"dia": 6, "valor": 2500},
        {"dia": 7, "valor": null}, # sem faturamento
        {"dia": 8, "valor": 3000},
        {"dia": 9, "valor": null},  # Dia sem faturamento
        {"dia": 10, "valor": 3000},
        {"dia": 11, "valor": 3500},
        {"dia": 12, "valor": 4000},
        {"dia": 13, "valor": 2000},
        {"dia": 14, "valor": 2500}
    ]
}

import json

# Calcular o faturamento
def calcular_faturamento(faturamentos):
    if not faturamentos:
        return None, None, 0

    faturamentos_validos = [f['valor'] for f in faturamentos if f['valor'] is not None]

    if not faturamentos_validos:
        return None, None, 0

    # Menor e o maior valor de faturamento
    menor_faturamento = min(faturamentos_validos)
    maior_faturamento = max(faturamentos_validos)

    # Média mensal
    media_mensal = sum(faturamentos_validos) / len(faturamentos_validos)

    # Dias com faturamento acima da média
    dias_acima_da_media = sum(1 for f in faturamentos_validos if f > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Arquivo JSON
with open('faturamento.json', 'r') as file:
    dados = json.load(file)

# Obtém a lista de faturamentos
faturamentos = dados['faturamento']

# Calcula o resultado
menor, maior, dias_acima = calcular_faturamento(faturamentos)

# Resultado
print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")
