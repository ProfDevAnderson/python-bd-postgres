class Aluno:

    def __init__(self, id, nome, telefone):
        self.id = id
        self.nome = nome
        self.telefone = telefone

    def getNome(self):
        return self.nome

    def getTelefone(self):
        return self.telefone

    def getId(self):
        return self.id
