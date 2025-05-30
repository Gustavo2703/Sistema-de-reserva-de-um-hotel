# 🏨 Sistema de Reservas de um Hotel

Este é um sistema de gerenciamento de reservas de quartos de hotel, desenvolvido em Python com interface gráfica usando Tkinter. Ele permite ao usuário visualizar os quartos disponíveis, fazer e cancelar reservas, além de salvar e carregar os dados do hotel em um arquivo JSON.

---

## 🎯 Definição do Problema

Hotéis pequenos ou médios frequentemente não possuem sistemas digitais simples para controlar reservas, o que resulta em falhas como overbooking, perda de controle de disponibilidade ou dificuldade em manter histórico de clientes.  
Este projeto visa solucionar esse problema, oferecendo uma ferramenta funcional e intuitiva para a **gestão de reservas de hotel**.

---

## 🧪 Casos de Uso

### ✅ Caso de uso 1 – Fazer uma reserva
O usuário seleciona um quarto disponível na interface gráfica, informa o nome do cliente e o número de dias. O sistema realiza a reserva e atualiza o status do quarto.

### ✅ Caso de uso 2 – Cancelar uma reserva
O usuário seleciona uma reserva ativa e a cancela. O quarto é marcado novamente como disponível.

### ✅ Caso de uso 3 – Salvar dados
O sistema salva todas as informações (quartos e reservas) em um arquivo JSON dentro da pasta `data/`.

### ✅ Caso de uso 4 – Carregar dados
Ao carregar o sistema, o usuário pode carregar os dados previamente salvos para continuar a administração do hotel sem perda de informações.

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.12**
- **Tkinter** (interface gráfica)
- **JSON** (persistência dos dados)
- Paradigmas de **Programação Orientada a Objetos**

---

## 🚀 Como Executar

1. Certifique-se de que você tem **Python 3.12 ou superior** instalado.
2. Clone ou baixe o repositório.
3. Execute o arquivo da interface:

```bash
python interface.py
````

> O sistema abrirá uma janela gráfica com as opções de reserva, cancelamento e manipulação de dados.

---

## 📁 Estrutura do Projeto

```
RESERVA_HOTEL/
├── package/
│   ├── main.py       # Ponto de entrada via terminal
│   ├── gui.py        # Ponto de entrada via interface gráfica
│   ├── data/
│   │   └── dados_hotel.json  #Arquivos com dados persistidos
│   ├── models/
│       ├── hotel.py   # Classe Hotel
│       ├── quarto.py  # Hierarquia de Quartos
│       └── reserva.py  # Classe Reserva
│   
└── README.md
```

---

## 🔁 Relacionamentos POO

O projeto foi desenvolvido usando princípios da **Programação Orientada a Objetos**, com os seguintes relacionamentos:

* **Herança**:
  A classe `Quarto` é a superclasse de `Standard`, `Familia` e `Luxo`. Cada uma redefine os atributos padrão como valor e capacidade.

* **Agregação**:
  A classe `Hotel` agrega uma lista de objetos `Quarto` e uma lista de objetos `Reserva`.

* **Composição**:
  Cada objeto `Reserva` contém um objeto `Quarto` como parte de sua definição.

* **Polimorfismo**:
  O sistema aplica polimorfismo através do método calcularPreco(), que possui implementações diferentes nas subclasses de Quarto. Enquanto a classe Standard calcula o valor base, Familia aplica descontos para estadias longas e Luxo adiciona taxas premium.

---

## 📌 Funcionalidades

* Interface gráfica com Tkinter
* Cadastro e visualização de quartos por tipo
* Realização e cancelamento de reservas
* Listagem de reservas ativas
* Salvamento e carregamento dos dados em JSON
* Organização do sistema em módulos reutilizáveis

---

## 💡 Melhorias Futuras

* Interface com autenticação de usuário (login)
* Notificações de reserva
* Integração com banco de dados
* Relatórios automáticos de ocupação e faturamento

---

## 👤 Autor

Gustavo Bonifácio de Oliveira - 241025659

```

