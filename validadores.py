def validar_cpf(cpf):
    cpf = ''.join(filter(str.isdigit, cpf))

    if len(cpf) != 11:
        return False

    if cpf == cpf[0] * 11:
        return False

    for i in range(9, 11):
        soma = sum(int(cpf[j]) * ((i + 1) - j) for j in range(i))
        digito = (soma * 10) % 11
        if digito == 10:
            digito = 0
        if digito != int(cpf[i]):
            return False
    return True


def validar_telefone(telefone):

    telefone = ''.join(filter(str.isdigit, telefone))

    if len(telefone) == 10:
        return True
    elif len(telefone) == 11:
        if telefone[2] == '9':
            return True
        else:
            return False
    else:
        return False

def validar_cep(cep):
    cep = ''.join(filter(str.isdigit, cep))
    return len(cep) == 8

def validar_nome_completo(nome):
    partes = nome.strip().split()
    return len(partes) >= 2