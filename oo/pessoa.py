class Pessoa:

    olhos = 2 #Atributo de classe ou atributo default

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

class Homem(Pessoa):
    pass

if __name__ == '__main__':

    rubson = Homem(nome='Rubson')
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
    raira.olhos = 1
    del raira.olhos
    print(raira.__dict__)
    print(rubson.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(rubson.olhos)
    print(raira.olhos)
    print(id(Pessoa.olhos), id(rubson.olhos), id(raira.olhos))
    print(Pessoa.metodo_estatico(), raira.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), raira.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(rubson, Pessoa))
    print(isinstance(rubson, Homem))