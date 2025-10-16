# Validação de Login com While
# Permita que o usuário tente fazer login até digitar a senha correta ("1234"). Mostre uma mensagem de erro a cada tentativa incorreta.
senha = ""
while senha != "1234":
    senha = str(input("Digite sua senha: "))
    print("Erro tentativa incorreta")
print("Senha correta")