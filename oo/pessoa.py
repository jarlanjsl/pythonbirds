class Pessoa:
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