from config.Database import Database


class AlunoDAO:

    def __init__(self):
        pass

    def deletar(self, id):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute("delete from aluno where id="+id)
        bd.commit()
        print("Aluno excluido com sucesso!")

    def listar(self):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from aluno")
        resultado = cursor.fetchall()
        print("Consulta feita com sucesso")
        return resultado


    def buscarAluno(self, id):
        bd = Database().conectar()
        cursor = bd.cursor()
        cursor.execute("select * from aluno where id = "+id)
        resultado = cursor.fetchone()
        print("Consulta feita com sucesso")
        return resultado








    def cadastrar(self, aluno):
    # 1 - Conectar com o banco de dados
        bd  = Database().conectar()
    # 2 - Receber o cursor do banco (responsavel pela execução do script)
        cursor = bd.cursor()
    # 3 - executar o script
        script = "insert into aluno (nome, telefone) values ('"+aluno.getNome()+"', '"+aluno.getTelefone()+"')"
        cursor.execute(script)
        bd.commit()
        print("Aluno cadastrado com sucesso!")
