# Questão 1
indice = 13
soma = 0
k = 0

while k < indice:
    k = k + 1
    soma = soma + k

print(soma)

# Questão 2
fibonacci = [0, 1]

num = int(input("Digite um número inteiro: "))

while fibonacci[-1] < num:
    proximo_valor = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(proximo_valor)

if num in fibonacci:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")


# Questão 3
# a) 1, 3, 5, 7, 9

# b) 2, 4, 8, 16, 32, 64, 128

# c) 0, 1, 4, 9, 16, 25, 36, 49

# d) 4, 16, 36, 64, 100

# e) 1, 1, 2, 3, 5, 8, 13

# f) 2,10, 12, 16, 17, 18, 19, 20

# Questão 4

distancia_total = 100  # km
velocidade_carro = 110  # km/h
velocidade_caminhao = 80  # km/h
tempo_pedagio = 5  # min

# Cálculo da distância percorrida
tempo_carro = distancia_total / velocidade_carro * 60  # minutos
distancia_carro = velocidade_carro * (tempo_carro - tempo_pedagio) / 60  # km
distancia_caminhao = distancia_total - distancia_carro

# Verifica qual está mais próximo de Ribeirão Preto
if distancia_carro < distancia_caminhao:
    print("O carro está mais próximo de Ribeirão Preto.")
else:
    print("O caminhão está mais próximo de Ribeirão Preto.")

# O carro percorre a distância de 100 km a uma velocidade de 110 km/h, o que leva cerca de 54,54 minutos. Como ele possui tag de pedágio, não precisa parar em nenhum pedágio.

# Já o caminhão percorre a mesma distância a uma velocidade de 80 km/h. Porém, ele leva 5 minutos a mais em cada um dos 2 pedágios, totalizando 10 minutos adicionais. Portanto, o tempo total de viagem do caminhão é de 65 minutos.

# Como os dois veículos estão se movendo em direções opostas, eles se encontrarão após percorrerem juntos uma distância equivalente a 100 km (distância entre as cidades). A partir daí, podemos calcular qual veículo está mais próximo de Ribeirão Preto.

# O carro percorreu 54,54 minutos x 110 km/h = 100 km. Portanto, ele estará exatamente na cidade de Franca quando se encontrar com o caminhão.

# Já o caminhão percorreu 65 minutos x 80 km/h = 86,67 km. Portanto, ele estará mais próximo de Ribeirão Preto quando se encontrar com o carro.

# Então o carro estará em Franca quando os veículos se cruzarem e que o caminhão estará mais próximo de Ribeirão Preto.


# Questão 5
string = "Hello, world!"

letras_invertidas = []

for i in range(len(string)-1, -1, -1):
    letras_invertidas.append(string[i])

# Convertendo a lista de caracteres invertidos em uma string novamente
string_invertida = ''.join(letras_invertidas)

print(string_invertida)
