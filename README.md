# projeto-media-alunos2
🎓 Projeto Média Alunos

Este é um programa simples em Python para calcular a média de 3 notas de um aluno e mostrar se ele está Aprovado, em Recuperação, ou Reprovado. Também inclui o cálculo da média ponderada, considerando diferentes pesos para as notas.

📜 Funcionalidades
Cálculo da média aritmética: O programa calcula a média simples das 3 notas fornecidas.
Aprovação: Se a média for maior ou igual a 6, o aluno é Aprovado.
Recuperação: Se a média estiver entre 5.0 e 6.0, o aluno fica em Recuperação.
Reprovação: Se a média for abaixo de 5.0, o aluno está Reprovado.
Média ponderada: Calcula a média com pesos diferentes: as duas primeiras notas têm peso 1, e a terceira nota tem peso 2.
🚀 Como Usar
Passos para rodar o programa:
Clone o repositório:

Abra o terminal e clone o repositório para sua máquina:

git clone https://github.com/SEU_USUARIO/projeto-media-alunos.git
Não se esqueça de substituir SEU_USUARIO pelo seu nome de usuário no GitHub.

Instale o Python:

Se você ainda não tem o Python instalado, pode fazer o download aqui.

Execute o programa:

No terminal, navegue até o diretório do projeto e execute o seguinte comando:


python main.py
O programa vai pedir para você inserir as 3 notas. Depois, ele calculará a média e exibirá a situação do aluno (Aprovado, Recuperação ou Reprovado).

Exemplo de Uso
Exemplo 1:


Digite a nota 1: 8.0
Digite a nota 2: 7.5
Digite a nota 3: 9.0
A média do aluno é: 8.17
Aprovado
Exemplo 2:

Digite a nota 1: 5.5
Digite a nota 2: 5.0
Digite a nota 3: 6.0
A média do aluno é: 5.38
Recuperação
🔍 Como Funciona
O programa pede ao usuário para inserir as 3 notas e depois calcula a média ponderada. As duas primeiras notas têm peso 1 e a terceira tem peso 2, o que significa que a última nota tem mais impacto no resultado final.

Depois de calcular a média, o programa verifica a situação do aluno com base na média:

Aprovado: Se a média for maior ou igual a 6.0.
Recuperação: Se a média for entre 5.0 e 6.0.
Reprovado: Se a média for abaixo de 5.0.
Código do Programa
python

# main.py

# Função para calcular a média ponderada
def calcular_media(notas):
    return (notas[0] + notas[1] + notas[2] * 2) / 4

# Função para obter as 3 notas do aluno
def obter_notas():
    notas = []
    for i in range(1, 4):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)
    return notas

# Função para exibir o resultado
def exibir_resultado(media):
    print(f"A média ponderada do aluno é: {media:.2f}")
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
🛠 Tecnologias Utilizadas
Python: Usado para desenvolver o programa.
Git: Para controle de versão e colaboração no desenvolvimento do código.
🤝 Contribuindo
Se quiser ajudar a melhorar o projeto, fique à vontade para fazer um fork e contribuir!

Faça um fork deste repositório.
Crie uma branch para a sua feature: git checkout -b feature/nova-feature.
Commit suas mudanças: git commit -m "Descrição do que foi feito".
Push para a sua branch: git push origin feature/nova-feature.
Abra um pull request com as suas alterações.
📄 Licença
Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para mais detalhes.

