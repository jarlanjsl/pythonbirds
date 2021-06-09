class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=29):
        self.idade = idade
        self.nome = nome
        self.filhos  = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    vinicios = Pessoa(nome='Vinicios')
    vitoria = Pessoa(vinicios, nome='Vitoria')
    print(Pessoa.cumprimentar(vitoria))
    print(id(vitoria))
    print(vitoria.cumprimentar())
    print(vitoria.nome)
    print(vitoria.idade)
    for filho in vitoria.filhos:
        print(filho.nome)
    vitoria.sobrenome = 'Alves'
    del vitoria.filhos
    vitoria.olhos = 1
    del vitoria.olhos
    print(vitoria.sobrenome)
    print(vitoria.__dict__)
    print(vinicios.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(vitoria.olhos)
    print(vinicios.olhos)
    print(id(Pessoa.olhos), id(vitoria.olhos), id(vinicios.olhos))