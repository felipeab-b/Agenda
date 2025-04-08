from pessoa import Pessoa

class Agenda():

    def __init__(self):
        self.contatos = []

    def add(self):
        print("--- Adicionar Novo Contato ---")
        name = input("Nome: ")
        tel = input("Telefone: ")
        mail = input("Email: ")
        print("-------------------------------")
        print(f"O contato {name} foi adicionado com sucesso!")
        print("-------------------------------")

        contato = Pessoa(name,tel,mail)
        self.contatos.append(contato)

    def list(self):
        if self.contatos:
            print("\n--- Lista de Contatos ---")
            for i,contato in enumerate(self.contatos,1):
                print(f"{i}. {contato.name}")
            print("-------------------------------")
        else:
            print("-------------------------------")
            print("A agenda está vazia!")  
            print("-------------------------------")

    def remove(self):
        print("-------------------------------")
        id = int(input("Qual o contato que quer apagar: "))
        print("-------------------------------")
        for i,contato in enumerate(self.contatos,1):
            if id == i:
                rm_name = contato.name
                self.contatos.remove(contato)
        print(f"O contato {rm_name} foi apagado com sucesso!")
        print("-------------------------------")

    def show(self):
        print("-------------------------------")
        id = int(input("Qual o contato que quer ver os detalhes: "))
        print("\n-------------------------------")
        for i,contato in enumerate(self.contatos,1):
            if id == i:
                contato.details()
        print("-------------------------------")

    def edit(self):
        print("-------------------------------")
        id = int(input("Qual o contato que quer editar: "))
        print("-------------------------------")
        print("O que quer editar? (nome, telefone, email)")
        opcao = input("Escolha a opção: ").lower()

        for i,contato in enumerate(self.contatos,1):
            if id == i:
                if opcao == 'nome':
                    contato.name = input("Novo nome: ")
                elif opcao == 'telefone':
                    contato.tel = input("Novo telefone: ")
                elif opcao == 'mail':
                    contato.mail = input("Novo email: ")
        print("-------------------------------")
        print("Contato editado!")
        print("-------------------------------")

    def loop(self):
        while True:
            print("\n--- Agenda de Contatos ---")
            print("1 - Adicionar Contato")
            print("2 - Mostrar Lista de Contatos")
            print("3 - Remover Contato")
            print("4 - Mostrar Detalhes de um Contato")
            print("5 - Editar Contato")
            print("6 - Sair")
            print("-------------------------------")
            x = int(input("O que deseja fazer: "))

            match x:
                case 1:
                    self.add()
                case 2:
                    self.list()
                case 3:
                    self.remove()
                case 4:
                    self.show()
                case 5:
                    self.edit()
                case 6:
                    print("Encerrando...")
                    break
                case _:
                    print("Insira uma opção válida !")


            