def ler_vetor():
    vetor = []
    for i in range(5):
        num = int(input(f"Digite o {i + 1}º número: "))
        vetor.append(num)
    return vetor


def calcular_c(a, b):
    vetor_c = []
    for i in range(5):
        if a[i] % 2 == 0:
            vetor_c.append(a[i] * b[i])
        else:
            vetor_c.append(a[i] * b[i] ** 2)
    return vetor_c


def imprimir_vetor(vetor, nome):
    print(f"Vetor {nome}: {vetor}")


def main():
    vetor_a = []
    vetor_b = []
    vetor_c = []

    while True:
        print("\n1. Ler vetores A e B")
        print("2. Calcular vetor C")
        print("3. Imprimir vetores")
        print("4. Sair")

        opcao = int(input("\nEscolha uma opção: "))

        if opcao == 1:
            vetor_a = ler_vetor()
            vetor_b = ler_vetor()
        elif opcao == 2:
            if not vetor_a or not vetor_b:
                print("Os vetores A e B devem ser lidos primeiro.")
            else:
                vetor_c = calcular_c(vetor_a, vetor_b)
                print("Vetor C calculado com sucesso.")
        elif opcao == 3:
            imprimir_vetor(vetor_a, "A")
            imprimir_vetor(vetor_b, "B")
            imprimir_vetor(vetor_c, "C")
        elif opcao == 4:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")


if __name__ == "__main__":
    main()
