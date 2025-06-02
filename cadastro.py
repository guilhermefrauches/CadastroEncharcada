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
        regiao = input("Região (Norte, Nordeste, Sul, Sudeste e Centro-Oeste): ").strip().lower()
        if regiao in ['norte', 'nordeste', 'sul', 'sudeste', 'centro-oeste']:
            regiao = regiao.capitalize()
            break
        else:
            print("Região inválida! Tente novamente.\n")

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
        "região": regiao,
        "cep": cep,
        "preferencia": preferencia
        
    }

    usuarios.append(usuario)
    print("\nUsuário cadastrado com sucesso!")
    print(f"Nome: {usuario['nome']}")
    print(f"CPF: {usuario['cpf']}")
    print(f"Email: {usuario['email']}")
    print(f"Telefone: {usuario['telefone']}")
    print(f"Região: {usuario['região']}")
    print(f"CEP: {usuario['cep']}")
    print(f"Preferência de aviso: {usuario['preferencia']}")
     
    print("\n📢 Aviso Regional:")
    regiao = regiao.lower()
    
    if regiao == 'sudeste':
        print("Atenção Região Sudeste: Chuva Forte em Áreas Urbanas.")
    elif regiao == 'nordeste':
        print("Atenção Região Nordeste: Acúmulo de Água em Regiões Costeiras.")
    elif regiao == 'norte':
        print("Atenção Região Norte: Nível dos Rios em Elevação.")
    elif regiao == 'sul':
        print("Atenção Região Sul: Possibilidade de Alagamentos Localizados.")
    elif regiao == 'centro-oeste':
        print("Aviso Região Centro-Oeste: Chuva Moderada com Risco Baixo de Alagamento.")