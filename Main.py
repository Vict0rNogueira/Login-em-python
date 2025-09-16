from dados import coletar_dados, mostrar_dados
from menu import selecionar_curso

def main():
    dados = coletar_dados()
    curso_final = selecionar_curso()
    mostrar_dados(dados, curso_final)

if __name__ == "__main__":
    main()
