class Pessoa:
    def __init__(self, *filhos, nome=None, idade=31):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    dylan = Pessoa(nome='Dylan')
    evanilson = Pessoa(dylan, nome='Evanilson')
    print(Pessoa.cumprimentar(evanilson))
    print(id(evanilson))
    print(evanilson.cumprimentar())
    print(evanilson.nome)
    print(evanilson.idade)
    for filho in evanilson.filhos:
        print(filho.nome)
    evanilson.sobrenome = 'Andrade dos Santos'
    del evanilson.filhos
    print(evanilson.__dict__)
    print(dylan.__dict__)