class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    vander = Pessoa(nome='Vander')
    Roberto = Pessoa(vander, nome='Roberto')
    print(Pessoa.cumprimentar(Roberto))
    print(id(Roberto))
    print(Roberto.cumprimentar())
    print(Roberto.nome)
    print(Roberto.idade)
    for filho in Roberto.filhos:
        print(filho.nome)
    print(Roberto.filhos)






