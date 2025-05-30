import tkinter as tk
from tkinter import messagebox, simpledialog
from package.models.hotel import Hotel
from package.models.quarto import Standard, Familia, Luxo

class HotelApp:
    def __init__(self, root):
        self.hotel = Hotel("Hotel Python")
        self.root = root
        self.root.title("Sistema de Reservas de Hotel")

       # Adiciona vários quartos
        for num in range(101, 106):
            self.hotel.adicionar_quarto(Standard(num))

        for num in range(201, 204):
            self.hotel.adicionar_quarto(Familia(num))

        for num in range(301, 304):
            self.hotel.adicionar_quarto(Luxo(num))

        # Listbox para quartos
        self.lista_quartos = tk.Listbox(root, width=50)
        self.lista_quartos.pack(pady=10)

        # Botões
        btn_frame = tk.Frame(root)
        btn_frame.pack()

        tk.Button(btn_frame, text="Reservar", command=self.reservar).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Cancelar", command=self.cancelar).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="Salvar", command=self.salvar).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Carregar", command=self.carregar).grid(row=0, column=3, padx=5)

        # Título da seção de reservas
        tk.Label(root, text="Reservas Ativas").pack(pady=5)

        self.lista_reservas = tk.Listbox(root, width=50)
        self.lista_reservas.pack(pady=5)

        self.atualizar_interface()

    def atualizar_interface(self):
        self.lista_quartos.delete(0, tk.END)
        for q in self.hotel.quartos:
            status = "Reservado" if q.reservado else "Disponível"
            self.lista_quartos.insert(tk.END, f"Quarto {q.numero} ({q.__class__.__name__}) - {status}")

        self.lista_reservas.delete(0, tk.END)
        for r in self.hotel.reservas:
            self.lista_reservas.insert(tk.END, f"{r.cliente} - Quarto {r.quarto.numero} ({r.dias} dias)")

    def reservar(self):
        try:
            selection = self.lista_quartos.curselection()[0]
            quarto = self.hotel.quartos[selection]
        except IndexError:
            messagebox.showerror("Erro", "Selecione um quarto.")
            return

        if quarto.reservado:
            messagebox.showwarning("Indisponível", "Quarto já reservado.")
            return

        cliente = simpledialog.askstring("Cliente", "Nome do cliente:")
        if not cliente:
            return
        try:
            dias = int(simpledialog.askstring("Dias", "Número de dias:"))
        except:
            messagebox.showerror("Erro", "Número inválido.")
            return

        self.hotel.fazer_reserva(quarto.numero, cliente, dias)
        self.atualizar_interface()

    def cancelar(self):
        try:
            selection = self.lista_reservas.curselection()[0]
            reserva = self.hotel.reservas[selection]
        except IndexError:
            messagebox.showerror("Erro", "Selecione uma reserva.")
            return

        self.hotel.cancelar_reserva(reserva.quarto.numero)
        self.atualizar_interface()

    def salvar(self):
        try:
            self.hotel.salvar_no_arquivo()
            messagebox.showinfo("Sucesso", "Dados salvos com sucesso!")
        except:
            messagebox.showerror("Erro", "Erro ao salvar arquivo.")

    def carregar(self):
        try:
            self.hotel = Hotel.carregar_do_arquivo()
            messagebox.showinfo("Sucesso", "Dados carregados com sucesso!")
            self.atualizar_interface()
        except FileNotFoundError:
            messagebox.showwarning("Aviso", "Arquivo não encontrado.")

# Inicializa a interface
if __name__ == "__main__":
    root = tk.Tk()
    app = HotelApp(root)
    root.mainloop()