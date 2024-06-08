'''Questão 5
Escreva uma função main que pergunte a distância que um passageiro deseja percorrer em km. Calcule o preço da passagem,
cobrando R$ 0.50 por km para viagens de até 200 km, R$ 0.45 para viagens entre 200 e 400 km e para viagens mais longas 
será cobrado R$ 0.35 por km.'''

def main():
    dist = int(input(f"Qual a distância você irá percorrer? (em km)  "))
    if dist <= 200:
        return dist * 0.5
    if (dist > 200) & (dist <= 400):
        return dist * 0.45
    else:
        return dist * 0.35
