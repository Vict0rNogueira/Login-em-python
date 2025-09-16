from utils import erro_dado

def coletar_dados():
    return {
        "Nome": input("Insira seu nome: "),
        "Matrícula": erro_dado("Insira sua matrícula: "),
        "Idade": erro_dado("Insira sua idade: ")
    }

def mostrar_dados(dados, curso):
    print("\n== Dados Do Usuário ==")
    print(f"Nome: {dados['Nome']}")
    print(f"Matrícula: {dados['Matrícula']}")
    print(f"Idade: {dados['Idade']}")
    if curso:
        print(f"Curso escolhido: {curso}")
    else:
        print("Nenhum curso foi selecionado.")
