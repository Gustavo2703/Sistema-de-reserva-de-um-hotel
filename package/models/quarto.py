class Quarto:
    def __init__(self, numero: int, capacidade: int, valor: int) -> None:
        self.numero = numero
        self.capacidade = capacidade
        self.valor = valor
        self.reservado = False

    def calcular_preco(self, dias) -> int:
        return (self.valor * dias)
    
    def reservar(self) -> bool:
        if not self.reservado:
            self.reservado = True
            return True
        return False
    
    def liberar(self) -> bool:
        if self.reservado:
            self.reservado = False
            return True
        return False
    
class Standard(Quarto):
    def __init__(self, numero: int, capacidade: int = 2, valor: int = 200):
        super().__init__(numero, capacidade, valor)

class Familia(Quarto):
    def __init__(self, numero: int, capacidade: int = 4, valor: int = 250):
        super().__init__(numero, capacidade, valor)

    def calcular_preco(self, dias):
        if dias >= 5:
            return ((self.valor * dias) * 0.90)  # 10% de desconto
        return (self.valor * dias)
    
class Luxo(Quarto):
    def __init__(self, numero: int, capacidade: int = 2, valor: int = 300):
        super().__init__(numero, capacidade, valor)

    def calcular_preco(self, dias):
        return ((self.valor * dias) * 1.10)  # 10% de acréscimo