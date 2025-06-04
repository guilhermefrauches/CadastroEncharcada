from cadastro import cadastrar

WHITE_BOLD = "\033[1;37m"
RESET   = "\033[0m"

print(f"{WHITE_BOLD}Olá, bem-vindo ao sistema de cadastro da Encharcada!{RESET}")
print(f"{WHITE_BOLD}Por favor, preencha as informações abaixo para se cadastrar{RESET}\n")

cadastrar()
print (f"{WHITE_BOLD}Obrigado por se cadastrar! Até logo!{RESET}\n")