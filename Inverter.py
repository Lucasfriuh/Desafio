# Função para inverter um texto
def inverter_texto(s):
    resultado = ""
    for i in range(len(s) - 1, -1, -1):
        resultado += s[i]
    return resultado

# Entrada do texto pelo usuário
entrada_usuario = input("Digite o texto para inverter: ")

# Inversão do texto
texto_invertida = inverter_texto(entrada_usuario)

# Exibição do resultado
print(f"Texti invertido: {texto_invertida}")