from .quarto import *

class Reserva:
    def __init__(self, quarto: Quarto, cliente: str, dias: int):
        self.quarto = quarto
        self.cliente = cliente
        self.dias = dias
        self.valor_total = quarto.calcular_preco(dias)

    def __str__(self):
        return (
            f"Reserva - Quarto {self.quarto.numero}\n"
            f"Cliente: {self.cliente}\n"
            f"{self.dias} dias | Total: R${self.valor_total:.2f}"
        )