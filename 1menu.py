from Cidades import Cidades
from times import Times
from main import Dicas

def escolher():
    print("Jogos disponíveis: "
              "1.Jogadores\n"
              "2.Cidades\n"
              "3.Times\n")
    escolha = input("Digite o número do jogo desejado: ")
    if escolha == "1":
        j = Dicas()
        j.sortear_palavra()

    if escolha == "2":
        a =Cidades()
        a.sortear_city()
    if escolha == "3":
        t = Times()
        t.sortear_times()


escolher()