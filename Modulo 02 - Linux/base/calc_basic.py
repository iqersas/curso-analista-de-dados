def ler_numero(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(
                "Erro! O caractere digitado não é um número. Por favor, tente novamente."
            )


def calcular(op, num1, num2):
    operations = {
        "1": lambda: num1 + num2,
        "2": lambda: num1 - num2,
        "3": lambda: num1 * num2,
        "4": lambda: num1 / num2,
    }
    if op in operations:
        return operations[op]()
    else:
        raise ValueError("Operação inválida. Por favor, tente novamente.")


def main():
    while True:
        print("Bem vindo! Para iniciar, por favor escolha uma das seguintes opções:")
        print("1 - Soma")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("-------------------")
        print("0 - Sair\n")
        op = input("Por favor digite o número equivalente a operação desejada: ")
        if op not in ["1", "2", "3", "4", "0"]:
            print("Erro! Opção inválida!")
            continue

        if op == "0":
            print("Encerrando o programa...")
            break

        num1 = ler_numero("Primeiro número: ")
        num2 = ler_numero("Segundo número: ")

        try:
            resultado = calcular(op, num1, num2)
            if resultado % 1 == 0:
                print(f"O resultado da operação é: {int(resultado)}")
                if (
                    input("Deseja converter o resultado para decimal? (s/n): ")
                    .strip()
                    .lower()
                    == "s"
                ):
                    print(
                        f"O resultado da operação em decimal é: {format(float(resultado), '.2f')}"
                    )
            else:
                print(f"O resultado da operação é: {format(resultado, '.2f')}")
                if (
                    input("Deseja converter o resultado para inteiro? (s/n): ")
                    .strip()
                    .lower()
                    == "s"
                ):
                    print(
                        f"O resultado da operação em inteiro é: {int(float(resultado))}"
                    )
        except ZeroDivisionError:
            print("Erro! Divisão por zero!")
        except ValueError as e:
            print(f"Erro! {e}")

        if input("Deseja fazer outra operação? (s/n): ").strip().lower() != "n":
            continue

        print("Encerrando o programa...")
        break


if __name__ == "__main__":
    main()
