print("Olá campeão, bem-vindo ao meu primeiro projeto por conta própria!")
print("Este é um sistema de dados simples e versátil com finalidade de demonstrar e fixar meus conhecimentos.")

nome = input("Digite o seu nome: ")
if nome == "":
    print("Erro: você precisa digitar suas informações para o sistema rodar!")
    exit()

idade = input("Digite sua idade: ")
if idade == "":
    print("Erro: você precisa digitar suas informações para o sistema rodar!")
    exit()

time_favorito = input("Digite seu time do coração: ")
if time_favorito == "":
    print("Erro: você precisa digitar suas informações para o sistema rodar!")
    exit()

print(f"Seu nome é: {nome}, tem {idade} anos e seu time é {time_favorito}")

