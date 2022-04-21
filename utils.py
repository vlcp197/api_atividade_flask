from models import Pessoas

def insere_pessoas():
    pessoa = Pessoas(nome='Vinicius',idade='25')
    print(pessoa)

def consulta():
    pass

if __name__ == '__main__':
    insere_pessoas()