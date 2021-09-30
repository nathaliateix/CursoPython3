# Aula 07 - Introdução à formatação de Strings
nome = 'Nathalia'
idade = 26
altura = 1.72
peso = 58
imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu IMC é', round(imc, 2))
print(f'{nome} tem {idade} anos de idade e seu IMC é {imc:.2f}')
print('{} tem {} anos de idade e sei IMC é {:.2f}'.format(nome, idade, imc))
