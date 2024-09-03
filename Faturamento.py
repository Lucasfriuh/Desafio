# Função que calcula o menor e o maior valor de faturamento e o número de dias com faturamento acima da média
def calcular_faturamento(faturamentos):
    if not faturamentos:
        return None, None, 0

    # Calculando o menor e o maior valor de faturamento
    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    
    # Calculando a média mensal
    media_mensal = sum(faturamentos) / len(faturamentos)
    
    # Contando o número de dias com faturamento acima da média
    dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)
    
    return menor_faturamento, maior_faturamento, dias_acima_da_media

# Exemplo de vetor de faturamento diário
faturamentos = [1000, 1500, 2000, 2500, 3000, 3500, 4000, 4500, 5000, 2250, 2750, 3000]

# Chamando a função e armazenando os resultados
menor, maior, dias_acima = calcular_faturamento(faturamentos)

# Imprimindo os resultados
print(f"Menor valor de faturamento: {menor}")
print(f"Maior valor de faturamento: {maior}")
print(f"Número de dias com faturamento acima da média: {dias_acima}")
