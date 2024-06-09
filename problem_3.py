'''Escreva um programa que solicite repetidamente que digite um número, os números serão 
somados e o programa será finalizado quando digitar o número 0. Ao final o programa 
retorna a soma dos números inseridos.'''

soma = 0

x = int(input(f"Digite um número: "))

while x != 0:
    soma += x
    x = int(input(f"Digite um número: "))

print(f"Soma: {soma}")