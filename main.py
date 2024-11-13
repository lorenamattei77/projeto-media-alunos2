# main.py

# Função para calcular a média aritmética
def calcular_media(notas):
    return sum(notas) / len(notas)

# Função para obter as notas do usuário
def obter_notas():
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)
    return notas

# Função para exibir o resultado
def exibir_resultado(media):
    print(f"A média do aluno é: {media:.2f}")
    if media >= 6.0:
        print("Aprovado")
    elif media >= 5.0:
        print("Recuperação")
    else:
        print("Reprovado")

# Função principal
if __name__ == "__main__":
    notas = obter_notas()
    media = calcular_media(notas)
    exibir_resultado(media)