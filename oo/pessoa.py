class Pessoa:
    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':

    rubson = Pessoa(nome='Rubson')
    raira = Pessoa(rubson, nome='Raira')
    print(Pessoa.cumprimentar(rubson))
    print(id(rubson))
    print(rubson.cumprimentar())
    print(rubson.nome)
    print(rubson.idade)
    for filho in raira.filhos:
        print(filho.nome)

    raira.sobrenome = 'Lima'
    print(raira.sobrenome)

    del raira.filhos
    print(raira.__dict__)
    print(rubson.__dict__)

