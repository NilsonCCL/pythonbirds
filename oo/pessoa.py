class Pessoa:

    olhos = 2

    def __init__(self, *filhos, nome=None, idade=31):
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


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    dylan = Homem(nome='Dylan')
    evanilson = Mutante(dylan, nome='Evanilson')
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
    print(Pessoa.olhos)
    print(evanilson.olhos)
    print(dylan.olhos)
    print(id(Pessoa.olhos), id(evanilson.olhos), id(dylan.olhos),)
    print(Pessoa.metodo_estatico(), evanilson.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), evanilson.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(evanilson, Pessoa))
    print(isinstance(evanilson, Homem))
    print(evanilson.olhos)
