# Exercicio 1
from cmath import pi


print('Python na Esola de Programacao Alura\n')

# Exercicio 2
nome = 'Luis Gustavo'
idade = 18
print(f'Meu nome é : {nome} e eu tenho {idade} anos\n')

# Exercicio 3
print('''
      A
      L
      U
      R
      A
      ''')

# Exercicio 4
print(f'O valor arredondado de pi é: {pi:.2f}')



# Exercícios Mod 2
# 1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
num = int(input('Digite um numero: '))
if num%2 == 0:
    print(f'O numeo {num} é par')
else:
    print(f'O numeo {num} é impar')


# 2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo 
# com as seguintes condições:
# Criança: 0 a 12 anos;
# Adolescente: 13 a 18 anos;
# Adulto: acima de 18 anos.
idade = int(input('Digite sua idade:'))
if idade>0 and idade<=12:
    print('Voçê é uma criança')
elif idade>12 and idade<18:
    print('Voçê é um adoslecente')
else:
    print('Voçê é um adulto')     

# 3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos 
# correspondem aos valores esperados determinados por você.

# 4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma e
# strutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

# Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
# Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
# Terceiro Quadrante: os valores de x e y devem ser menores que zero;
# Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
# Caso contrário: o ponto está localizado no eixo ou origem.