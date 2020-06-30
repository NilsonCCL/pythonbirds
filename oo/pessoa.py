class Pessoa:
    olhos = 2
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
    evanilson.olhos = 1
    del evanilson.olhos
    print(evanilson.__dict__)
    print(dylan.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(evanilson.olhos)
    print(dylan.olhos)
    print(id(Pessoa.olhos), id(evanilson.olhos), id(dylan.olhos),)