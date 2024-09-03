# Solicita ao usuário que informe um número
numero = int(input("Informe um número: "))

# Variáveis iniciais para a sequência de Fibonacci( no caso sendo 0 e 1)
fib1, fib2 = 0, 1
pertence = False

# Verifica se o número pertence a sequência de Fibonacci
if numero == fib1 or numero == fib2:
    pertence = True
else:
    fib_atual = fib1 + fib2
    while fib_atual <= numero:
        if fib_atual == numero:
            pertence = True
            break
        # Atualiza os valores
        fib1, fib2 = fib2, fib_atual
        fib_atual = fib1 + fib2

# Resultado
if pertence:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
