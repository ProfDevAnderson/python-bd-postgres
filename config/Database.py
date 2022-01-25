import psycopg2

class Database:

    def __init__(self):
        self.bd = None

    def conectar(self):
       self.bd = psycopg2.connect(host="localhost", database="IFMA",
                         user="postgres", password="postgres")
       print("Conexao Realizada com sucesso!")
       return self.bd

    def desconectar(self):
        self.bd.close()
