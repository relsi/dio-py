class Bicicleta:
    def __init__(self, cor, modelo, ano, valor, aro):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"

    def buzinar(self):
        print("plim... plim...")

    def parar(self):
        print("parando a bicicleta")
        print("bicicleta parada")
    
    def correr(self):
        print("runnnnnn....")

b1 = Bicicleta("vermelha", "caloi", 1982, 600, 16)
b1.buzinar()
b1.correr()
b1.parar()

print(b1)