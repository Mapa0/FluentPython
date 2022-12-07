import collections
from random import choice
#Uso da biblioteca collections para estabelecer nossa propria coleção.

#Esse programa mostra as vantagens de utilizar métodos especiais para aproveitar o modelo de dados do python.

Card = collections.namedtuple('Card', ['valor','naipe'])
#Utilizamos o collections.namedtuple para construir uma simple classe para representar cartas individuais.
#O namedtuple é utilizado para construir classes de objetos que são apenas conjuntos de atributos sem métodos, como um registro de BD.

class Baralho:
    valores = [str(n) for n in range(2,11)] + list('JQKA')
    naipes = 'espadas ouros paus copas'.split()

    def __init__(self):
        self._cartas = [
            Card(valor, naipe) 
            for valor in self. valores 
            for naipe in self.naipes]

#A Dunder Function __len__ faz com que nossa classe possa retornar um valor ao ser lida pela função len()
#Ou seja, se comporta como uma collection tradicional e retorna o número de cartas nele.
    def __len__(self):
        return len(self._cartas)

#A função Dunder __getitem__ permite o acesso rápido das cartas utilizando apenas o índice.
#Podendo ser lido como uma lista: baralho[0] retornaria a primeira carta do baralho enquanto baralho[-1] retornaria o último, por exemplo!
    def __getitem__(self, posicao):
        return self._cartas[posicao]

if __name__ == '__main__':
    baralho = Baralho()
    print(choice(baralho))
    #Podemos pegar uma carta aleatória utilizando a função choice!
    #Melhor ainda, como nosso __getitem__ delega o operador[] de self._cartas, nosso baralho automaticamente permite fatiamento.
    print(baralho[:3])
    print(baralho[12:13])
    #Além disso, é possível iterar pelas cartas do baralho:
    for carta in baralho:
        print(carta)
    #Ou então iterar pelo baralho ao contrário:
    for carta in reversed(baralho):
        print(carta)
    #I
    