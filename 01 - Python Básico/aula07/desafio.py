# Desafio prático
nome = 'Nathalia'
idade = 26
altura = 1.72
peso = 58
imc = peso / altura ** 2
ano_atual = 2021
ano_nascimento = ano_atual - idade

print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso}kg.')
print(f'O IMC de {nome} é {imc:.2f}.')
print(f'{nome} nasceu em {ano_nascimento}.')
