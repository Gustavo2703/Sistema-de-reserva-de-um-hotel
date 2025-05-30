from package.models.hotel import *
from package.models.quarto import Standard, Familia, Luxo

def mostrar_menu():
    print("\n=== Sistema de Reservas ===")
    print("1. Listar quartos")
    print("2. Fazer reserva")
    print("3. Cancelar reserva")
    print("4. Listar reservas")
    print("5. Salvar dados")
    print("6. Carregar dados")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    # Inicializa o hotel
    hotel = Hotel("Hotel Python")
    
    # Adiciona vários quartos
    for num in range(101, 106):
        hotel.adicionar_quarto(Standard(num))

    for num in range(201, 204):
        hotel.adicionar_quarto(Familia(num))

    for num in range(301, 304):
        hotel.adicionar_quarto(Luxo(num))

    while True:
        opcao = mostrar_menu()
        
        if opcao == "1":
            print("\n=== Quartos ===")
            for q in hotel.quartos:
                status = "Reservado" if q.reservado else "Disponível"
                print(f"Quarto {q.numero} ({q.__class__.__name__}) - {status}")
        
        elif opcao == "2":
            print("\n=== Nova Reserva ===")
            numero = int(input("Número do quarto: "))
            cliente = input("Nome do cliente: ")
            dias = int(input("Dias de hospedagem: "))
            
            reserva = hotel.fazer_reserva(numero, cliente, dias)
            if reserva:
                print(f"\nReserva confirmada!\n{reserva}")
            else:
                print("\nQuarto não disponível ou não encontrado.")
        
        elif opcao == "3":
            print("\n=== Cancelar Reserva ===")
            numero = int(input("Número do quarto: "))
            if hotel.cancelar_reserva(numero):
                print("Reserva cancelada com sucesso!")
            else:
                print("Nenhuma reserva encontrada para este quarto.")
        
        elif opcao == "4":
            print("\n=== Reservas Ativas ===")
            if not hotel.reservas:
                print("Nenhuma reserva ativa.")
            for r in hotel.reservas:
                print(r)
                print("-" * 20)
        
        elif opcao == "5":
            hotel.salvar_no_arquivo()
            print("Dados salvos com sucesso!")
        
        elif opcao == "6":
            try:
                hotel = Hotel.carregar_do_arquivo()
                print("Dados carregados com sucesso!")
            except FileNotFoundError:
                print("Arquivo não encontrado. Criando novo hotel.")
        
        elif opcao == "0":
            print("Saindo do sistema...")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()