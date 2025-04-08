class Pessoa():

    def __init__(self,name,tel,mail):
        self.name = name
        self.tel = tel
        self.mail = mail

    def details(self):
        print(f"Nome: {self.name}")
        print(f"Telefone: {self.tel}")
        print(f"Email: {self.mail}")