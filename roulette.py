
'''
Aluno: Mateus Henrique Machado 

'''

import random

#Função geral para o cálculo da rodada
def rodada(num):
    if num == "0" or num == "00":
        if num == "0":
            print("Pagar 0")
        else:
            print("Pagar 00")
    else:
        print(f"Pagar {num}")
        print(f"Pagar {cor(num)}")
        print(f"Pagar {tipo(num)}")
        print(f"Pagar {intervalo(num)}")

#Verificação de qual categoria de cor o número está 
def cor(num):
    if num in vermelho:
        return "vermelho"
    else:
        return "preto"

#Verificação se o número e ímpar ou par
def tipo(num):
    valor = int(num)
    if valor%2 == 0: 
        return "par"
    else:
        return "ímpar"

#Verificação do intervalo que o número está inserido 
def intervalo(num):
    if num in range(1,18):
        return "1 a 18"
    else:
        return "19 a 36"

#Declaração dos conjuntos 
verde = ["0", "00"]
vermelho = ["1", "3", "5", "7", "9", "12", "14", "16", "18", "19", "21", "23", "25", "27", "30", "32", "34", "36"]
roleta = ["0", "00"]

#Construção dos possíveis resultados na roleta
for i in range(36):
   roleta.append(str(i+1)) 

#Sorteio de um número aleatório 
num = str(random.choice(roleta))
print(f"O número sorteado foi: {num}")

rodada(num)