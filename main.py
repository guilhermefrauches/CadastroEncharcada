from cadastro import cadastrar

print("Olá, bem-vindo ao sistema de cadastro da Encharcada!")
print("Por favor, preencha as informações abaixo para se cadastrar.\n")

while True:
    cadastrar()
    continuar = input("\nDeseja cadastrar outro usuário? (s/n): ").strip().lower()
    if continuar != 's':
        print("Obrigado por se cadastrar! Até logo!")
        break
