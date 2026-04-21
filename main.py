import string
import random

def gerar_senha(tamanho):
    if tamanho < 4:
        print("O tamanho da senha deve ser pelo menos 4 caracteres.")
        return
    else:
        senha = [
            random.choice(string.ascii_letters), #letras
            random.choice(string.digits),        #números
            random.choice(string.punctuation)    #caracteres especiais
        ]
        possibilidades = "".join([string.ascii_letters, string.digits, string.punctuation]) #todas as possibilidades de caracteres
        senha.extend(random.choices(possibilidades, k=tamanho - 3)) #adiciona os caracteres restantes

        random.shuffle(senha) #embaralha a senha para garantir que os caracteres obrigatórios não fiquem sempre no início
        return "".join(senha) #converte a lista de caracteres em uma string e retorna a senha gerada
    
tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
print(gerar_senha(tamanho_senha))
