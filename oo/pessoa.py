class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    vander = Pessoa(nome= 'Vander')
    fabiano = Pessoa(vander, nome='Fabiano')
    print(Pessoa.cumprimentar(fabiano))
    print(id(fabiano))
    print(fabiano.cumprimentar())
    print(fabiano.nome)
    print(fabiano.idade)
    for filho in fabiano.filhos:
        print(filho.nome)