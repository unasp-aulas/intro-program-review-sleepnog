'''Escreva uma função main que calcule o aumento de um salário. Ele deve solicitar o valor
do salário (salario) e o nível do cargo (cargo). Cargo junior terá um aumento de 15%, 
pleno de 26% e senior 34%. A função deve retornar o novo salário. Caso o cargo não 
corresponda a nenhum dos 3, deverá ser retornado o valor -1.'''

def main(cargo, salario):
    if cargo == "junior":
        return salario * 1.5
    if cargo == "pleno":
        return salario * 2.6
    if cargo == "senior":
        return salario * 3.4
    else:
        return -1
    