class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("plim... plim...")

    def parar(self):
        print("parando a bicicleta")
        print("bicicleta parada")
    
    def correr(self):
        print("runnnnnn....")

b1 = Bicicleta("vermelha", "caloi", 1982, 600)
b1.buzinar()
b1.correr()
b1.parar()

print(b1.cor)