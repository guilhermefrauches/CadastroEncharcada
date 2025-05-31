from validadores import validar_cpf

usuarios = []

def cadastrar():
    nome = input("Nome completo: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    cep = input("CEP: ")
    preferencia = input("Preferência de aviso (email/sms/ambos): ")

    while True:
        cpf = input("CPF: ")
        if validar_cpf(cpf):
            break
        else:
            print("CPF inválido. Tente novamente.\n")

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