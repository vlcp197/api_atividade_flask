from models import Pessoas, db_session

# Insere dados na tabela pessoa
def insere_pessoas():
    pessoa = Pessoas(nome='Lima',idade='22')
    print(pessoa)
    pessoa.save()

# Realiza consulta na tabela pessoa
def consulta_pessoas():

    pessoa = Pessoas.query.all()
    print(pessoa)
    pessoa = Pessoas.query.filter_by(nome='Lima').first()
    print(pessoa.nome)

# Altera dados na tabela pessoa
def altera_pessoa():
     pessoa = Pessoas.query.filter_by(nome='Lima').first()
     pessoa.idade = 21 
     pessoa.save()

#Exclui dados na tabela pessoa
def exclui_pessoa():
     pessoa = Pessoas.query.filter_by(nome='Lima').first()
     pessoa.delete()


if __name__ == '__main__':
    #insere_pessoas()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoas()
    