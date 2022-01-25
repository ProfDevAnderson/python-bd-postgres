from model.Aluno import Aluno
from model.AlunoDAO import AlunoDAO

def cadastrar():
    nome = input("Qual o seu nome?")
    telefone = input("Qual o seu telefone?")
    aluno = Aluno(id=None, nome=nome, telefone=telefone)

    dao = AlunoDAO()
    dao.cadastrar(aluno)

def listar():
    dao = AlunoDAO()
    resultado = dao.listar()
    print(resultado)
    lista = list(map(lambda aluno: aluno[1], resultado))
    print(lista)

def buscar():
    id = input("Id do aluno:")
    dao = AlunoDAO()
    resultado = dao.buscarAluno(id)
    print("Dados da busca")
    print("nome: {} | Telefone {}".format(resultado[1], resultado[2]))

def deletar():
    id = input("Id do aluno para excluir:")
    dao = AlunoDAO()
    dao.deletar(id)

while(True):
    print("1- Cadastrar | 2 - Listar | 3 - Buscar | 4 - Excluir")
    opc = input("Selecione a opção desejada")
    if (opc == '1'):
        cadastrar()
    elif (opc == '2'):
        listar()
    elif (opc == '3'):
        buscar()
    elif (opc == '4'):
        deletar()

