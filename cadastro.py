from validadores import validar_cpf, validar_telefone,validar_cep,validar_nome_completo

usuarios = []

def cadastrar():
    while True:
        nome = input("Nome completo: ")
        if validar_nome_completo(nome):
            break
        else:
            print("Nome inválido! Tente novamente.\n")

    while True:
        cpf = input("CPF: ")
        if validar_cpf(cpf):
            break
        else:
            print("CPF inválido! Tente novamente.\n")

    while True:
        email = input("Email: ")
        if '@' in email and '.' in email:
            break
        else:
            print("Email inválido! Tente novamente.\n")
    
    while True:
        telefone = input("Telefone: ")
        if validar_telefone(telefone):
            break
        else:
            print("Telefone inválido! Tente novamente.\n")

    while True:
        cep = input("CEP: ")
        if validar_cep(cep):
            break
        else:
            print("CEP inválido! Tente novamente.\n")

    preferencia = input("Preferência de aviso (email/sms/ambos): ")


    usuario = {
        "nome": nome,
        "cpf": cpf,
        "email": email,
        "telefone": telefone,
        "cep": cep,
        "preferencia": preferencia
    }

    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!")
    print(f"Nome: {usuario['nome']}")
    print(f"CPF: {usuario['cpf']}")
    print(f"Email: {usuario['email']}")
    print(f"Telefone: {usuario['telefone']}")
    print(f"CEP: {usuario['cep']}")
    print(f"Preferência de aviso: {usuario['preferencia']}")