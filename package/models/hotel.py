import os
import json
from typing import List
from .quarto import *
from .reserva import Reserva

CAMINHO_ARQUIVO = os.path.join(
    os.path.dirname(__file__), "..", "data", "dados_hotel.json"
)

class Hotel:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.quartos: List[Quarto] = []
        self.reservas: List[Reserva] = []

    # Adiciona o objeto quarto a lista de quartos do hotel
    def adicionar_quarto(self, quarto: Quarto) -> None:
        self.quartos.append(quarto)

    # Busca o quarto na lista de quartos
    def buscar_quarto(self, numero: int) -> Quarto | None:
        for quarto in self.quartos:
            if quarto.numero == numero:
                return quarto
        return None
        
    # Realiza a reserva e a adiciona na lista
    def fazer_reserva(self, numero_quarto: int, cliente: str, dias: int) -> Reserva | None:
        quarto = self.buscar_quarto(numero_quarto)

        if quarto and not quarto.reservado:
            quarto.reservado = True
            reserva = Reserva(quarto, cliente, dias)
            self.reservas.append(reserva)
            return reserva
        return None
    
    # Cancela a reserva, caso ela exista
    def cancelar_reserva(self, numero_quarto: int) -> bool:
        for reserva in self.reservas:
            if reserva.quarto.numero == numero_quarto:
                reserva.quarto.reservado = False
                self.reservas.remove(reserva)
                return True
        return False
        
    # Salva as informações sobre o hotel em um arquivo json
    def salvar_no_arquivo(self, arquivo: str = CAMINHO_ARQUIVO) -> None:
        dados = {
            "nome": self.nome,
            "quartos": [
                { 
                    "numero": q.numero,
                    "tipo": q.__class__.__name__,
                    "capacidade": q.capacidade,
                    "valor": q.valor,
                    "reservado": q.reservado
                } for q in self.quartos],
            "reservas": [
                {
                    "quarto_numero": r.quarto.numero,
                    "cliente": r.cliente,
                    "dias": r.dias
                } for r in self.reservas]
        }

        with open(arquivo, "w") as f:
            json.dump(dados, f, indent = 4)

    # Carrega as informações que estão no arquivo json
    @classmethod
    def carregar_do_arquivo(cls, arquivo: str = CAMINHO_ARQUIVO):
        with open(arquivo, "r") as f:
            dados = json.load(f)

        hotel = cls(dados["nome"])

        tipos_de_quarto = {
            "Standard": Standard,
            "Familia": Familia,
            "Luxo": Luxo
        }

        for q in dados["quartos"]:
            quarto = tipos_de_quarto[q['tipo']](q['numero'], q['capacidade'], q['valor'])
            quarto.reservado = q['reservado']
            hotel.adicionar_quarto(quarto)
        
        for r in dados['reservas']:
            quarto = hotel.buscar_quarto(r['quarto_numero'])
            if quarto:
                reserva = Reserva(quarto, r['cliente'], r['dias'])
                hotel.reservas.append(reserva)
        
        return hotel