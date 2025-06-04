from validadores import validar_cpf, validar_telefone,validar_cep,validar_nome_completo, identificar_regiao_por_ddd
import re

#cores
RED     = "\033[31m"
GREEN   = "\033[32m"
BLUE    = "\033[34m"
RESET   = "\033[0m"
WHITE_BOLD = "\033[1;37m"
YELLOW  = "\033[33m"
DARK_GREEN = "\033[38;5;22m"

usuarios = []

def cadastrar():
    while True:
        nome = input(f"{WHITE_BOLD}Nome completo: {RESET}")
        if validar_nome_completo(nome):
            break
        else:
            print(f"{RED}Formato inválido! Tente Nome e Sobrenome.\n{RESET}")

    while True:
        cpf = input(f"{WHITE_BOLD}CPF: {RESET}")
        cpf_limpo = re.sub(r'\D', '', cpf)
        if validar_cpf(cpf_limpo):
         break
        else:
            print(f"{RED}CPF inválido! Tente novamente.\n{RESET}")

    while True:
        email = input(f"{WHITE_BOLD}Email: {RESET}")
        if '@' in email and '.' in email:
            break
        else:
            print(f"{RED}Email inválido! Tente novamente.\n {RESET}")
    
    while True:
        telefone = input(f"{WHITE_BOLD}Telefone: {RESET}")
        if validar_telefone(telefone):
            break
        else:
            print(f"{RED}Telefone inválido! Tente novamente.\n {RESET}")

    regiao = identificar_regiao_por_ddd(telefone)
    if not regiao:
        print(f"{RED}DDD não reconhecido. Região será marcada como 'Desconhecida'.{RESET}")  
        regiao = "Desconhecida"


    while True:
        cep = input(f"{WHITE_BOLD}CEP: {RESET}")
        if validar_cep(cep):
            break
        else:
            print(f"{RED}CEP inválido! Tente novamente.\n {RESET}")
    
    while True:
        preferencia = input(f"{WHITE_BOLD}Preferência de aviso ({GREEN}whatsapp{RESET}{WHITE_BOLD}/sms/{RESET}{BLUE}app{RESET}): ").strip().lower()
        if preferencia in ['whatsapp', 'sms', 'app']:
            break
        else:
            print(f"{RED}Preferência inválida! Tente novamente.\n{RESET}")


    usuario = {
        "nome": nome,
        "cpf": cpf_limpo,
        "email": email,
        "telefone": telefone,
        "região": regiao,
        "cep": cep,
        "preferencia": preferencia

    }

    usuarios.append(usuario)

    print(f"\n{DARK_GREEN}Usuário cadastrado com sucesso!{RESET}")
    print(f"{WHITE_BOLD}Nome: {usuario['nome']}{RESET}")
    print(f"{WHITE_BOLD}CPF: {usuario['cpf']}{RESET}")
    print(f"{WHITE_BOLD}Email: {usuario['email']}{RESET}")
    print(f"{WHITE_BOLD}Telefone: {usuario['telefone']}{RESET}")
    print(f"{WHITE_BOLD}Região: {usuario['região']}{RESET}")
    print(f"{WHITE_BOLD}CEP: {usuario['cep']}{RESET}")
    print(f"{WHITE_BOLD}Preferência de aviso: {usuario['preferencia']}{RESET}")
     
    
    print(f"\n📢 {YELLOW}Aviso Regional:{RESET}")
    regiao = regiao.lower()
    
    if regiao == 'sudeste':
        print(f"{WHITE_BOLD}Atenção Região Sudeste: Chuva Forte em Áreas Urbanas.{RESET}")
    elif regiao == 'nordeste':
        print(f"{WHITE_BOLD}Atenção Região Nordeste: Acúmulo de Água em Regiões Costeiras.{RESET}")
    elif regiao == 'norte':
        print(f"{WHITE_BOLD}Atenção Região Norte: Nível dos Rios em Elevação.{RESET}")
    elif regiao == 'sul':
        print(f"{WHITE_BOLD}Atenção Região Sul: Possibilidade de Alagamentos Localizados.{RESET}")
    elif regiao == 'centro-oeste':
        print(f"{WHITE_BOLD}Aviso Região Centro-Oeste: Chuva Moderada com Risco Baixo de Alagamento.{RESET}")