'''Escreva uma função main que crie uma sequencia de números e receba um argumento como 
ultimo número. O retorno da função deve ser a soma de todos estes números gerados.'''

def main(x):
    soma = 0
    for i in range(0, x+1):
        soma += i
    return soma