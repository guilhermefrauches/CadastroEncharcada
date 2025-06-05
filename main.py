from cadastro import cadastrar

WHITE_BOLD = "\033[1;37m"
YELLOW  = "\033[33m"
RESET   = "\033[0m"

print(f"{YELLOW}Olá, bem-vindo ao sistema de cadastro da Encharcada!{RESET}")
print(f"{YELLOW}Por favor, preencha as informações abaixo para se cadastrar{RESET}\n")

cadastrar()
print (f"{WHITE_BOLD}Obrigado por se cadastrar! Até logo!{RESET}\n")