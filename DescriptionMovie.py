import requests
import json
import time

vermelho = '\033[31;1m'
verde = '\033[32;1m'
azul = '\033[34;1m'
normal = '\033[0;0m'

banner = """
========================================
#Codedy by: SystX                      #
#date: 06/04/2017                      #
#Github: https://github.com/Elifelete  #
========================================
"""
print(azul + banner)


def requisicao(titulo):
    try:
        req = requests.get("http://www.omdbapi.com/?t=" + titulo)
        filme = json.loads(req.text)
        return filme

    except:
        print("Error na Conexão")
        return None


def printar_detalhes(filme):
    print("")
    print(verde + "# Titulo:", filme["Title"])
    print(verde + "# Ano:", filme["Year"])
    print(verde + "# Diretor:", filme["Director"])
    print(verde + "# Atores:", filme["Actors"])
    print(verde + "# Genero:", filme["Genre"])
    print(verde + "# Nota:", filme["imdbRating"])
    print(verde + "# Poster:", filme["Poster"]+ normal)

def pesguisa():

    op = input(azul + "Escreva o nome do filme: "+ normal).upper()

    filme = requisicao(op)
    if filme["Response"] == "False":
        print(vermelho + "Filme não encontrado" + normal)
    else:
        printar_detalhes(filme)
    rep = input(azul +"\nDeseja fazer outra busca sim ou nao: ")
    if rep == "sim" or rep == "s" or rep == "yes":
        pesguisa()
    else:
        print("saindo...")
        time.sleep(2)
        print("... bye")
        time.sleep(1)
        exit()

pesguisa()

