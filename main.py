import string
import random


def gerar_senha(tamanho: int) -> str:
    """Gera uma senha segura com letras, números e caracteres especiais."""
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser pelo menos 4 caracteres.")

    senha = [
        random.choice(string.ascii_letters),  # letra obrigatória
        random.choice(string.digits),          # número obrigatório
        random.choice(string.punctuation),     # especial obrigatório
    ]

    possibilidades = string.ascii_letters + string.digits + string.punctuation
    senha.extend(random.choices(possibilidades, k=tamanho - 3))

    random.shuffle(senha)
    return "".join(senha)


def main():
    while True:
        try:
            tamanho = int(input("Digite o tamanho da senha desejada: "))
            senha = gerar_senha(tamanho)
            print(f"Senha gerada: {senha}")
            break
        except ValueError as e:
            print(f"Erro: {e}. Tente novamente.")


if __name__ == "__main__":
    main()
