cursos = {
    1: "Python",
    2: "Java",
    3: "JavaScript",
    4: "C#"
}

def exibir_menu():
    print("\n== CURSOS ==")
    for chave, valor in cursos.items():
        print(f"{chave} - {valor}")
    print("0 - Sair")

def selecionar_curso():
    curso_selecionado = None
    while True:
        exibir_menu()
        try:
            opcao = int(input("Digite o número relacionado ao seu curso: "))
        except ValueError:
            print("Número escolhido inválido")
            continue

        if opcao == 0:
            print("Saindo...")
            break
        elif opcao in cursos:
            curso_selecionado = cursos[opcao]
            print(f"Curso selecionado: {curso_selecionado}")
        else:
            print("Opção inválida.")

    return curso_selecionado
