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

def identificar_regiao_por_ddd(telefone):
    import re
    ddd_match = re.search(r'\d{2}', telefone)
    if not ddd_match:
        return None
    ddd = int(ddd_match.group())

    match ddd:
        case 68 | 96 | 92 | 97 | 91 | 93 | 94 | 95 | 69 | 63:
            return "Norte"
        case 82 | 71 | 73 | 74 | 75 | 77 | 85 | 88 | 98 | 99 | 83 | 81 | 87 | 86 | 89 | 84 | 79:
            return "Nordeste"
        case 61 | 62 | 64 | 65 | 66 | 67:
            return "Centro-Oeste"
        case 27 | 28 | 31 | 32 | 33 | 34 | 35 | 37 | 38 | 21 | 22 | 24 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19:
            return "Sudeste"
        case 41 | 42 | 43 | 44 | 45 | 46 | 47 | 48 | 49 | 51 | 53 | 54 | 55:
            return "Sul"
        case _:
            return None

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