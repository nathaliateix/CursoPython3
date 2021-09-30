# Aula 05 - Operadores Aritméticos
'''
+ -> Adição ou Concatenação 'str + str'
- -> Subtração
* -> Multiplicação ou Repetição 'int * str'
/ -> Divisão Real
// -> Divisão Inteira 'Arredonda o valor'
** -> Exponenciação
% -> Retorna um módulo 'Resto de uma divisão'
() -> Alterar a precedência nas contas
'''
print(10 + 10, '-> Adição')
print('10' + '10', '-> Concatenação')
print(10 - 5, '-> Subtração')
print(10 * 5, '-> Multiplicação')
print(10 * 'A', '-> Repetição')
print(10 / 4, '-> Divisão Real')
print(10 // 4, '-> Divisão Inteira')
print(2 ** 10, '-> Exponenciação')
print(10 % 4, '-> Módulo')
print((10 + 5) * 2, '-> Precedência')
print(2 + 5 * 3 ** 2 - (23.5 + 23.5), '-> Teste')
