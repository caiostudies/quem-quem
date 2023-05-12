import random


class Cidades():
    def __init__(self):
        ...


    def sao_paulo(self):
        self.dica1 = "1.É uma capital de estado"
        self.dica2 = "2.Tem a maior colônia japonesa fora do Brasil"
        self.dica3 = "3.Uma das cidades mais populosas do mundo"
        self.dica4 = "4.Normalmente as pessoas vão em busca de empregos"
        self.dica5 = "5.Conhecida pelo transito"

    def nova_york(self):
        self.dica1 = "1.Possui uma das sete maravilhas do mundo"
        self.dica2 = "2.Seu maior centro comercial pode ser visto até do espaço"
        self.dica3 = "3.Se localiza nos Estados Unidos"
        self.dica4 = "4.Nos filmes da Marvel é onde se localiza a casa dos Vingadores"
        self.dica5 = "5.Sofreu um grande atentado terrorista em 2001"

    def Londres(self):
        self.dica1 = "1.É uma capital de país"
        self.dica2 = "2.Possui apenas um time campeão de champions "
        self.dica3 = "3.É o local de nascimento de uma pessoa que você vê toda semana"
        self.dica4 = "4.Possui um grande relógio famoso"
        self.dica5 = "5.Sua língua oficial é o inglês"



    def sortear_city(self):
        cidades = ["São Paulo", "Nova York", "Londres"]
        city = random.choice(cidades)

        print(city)

        if city == "São Paulo":
            self.sao_paulo()
            print(self.dica1)
            resposta = input("Que cidade você acha que é: ")
            if resposta != city:
                print(self.dica2)
                resposta = input("Que cidade você acha que é: ")

            if resposta != city:
                print(self.dica3)
                resposta = input("Que cidade voce acha que é: ")

            if resposta != city:
                print(self.dica4)
                resposta = input("Que cidade voce acha que é: ")

            if resposta != city:
                print(self.dica5)
                resposta = input("Que cidade voce acha que é: ")

            if resposta != city:
                print("-----Suas chances acabaram!!!!----")

            elif resposta == city:
                print("------Parabéns voce acertou a palavra!!!!!!-------")

        if city == "Nova York":
            self.nova_york()
            print(self.dica1)
            resposta = input("Que cidade voce acha que é: ")
            if resposta != city:
                print(self.dica2)
                resposta = input("Que cidade você acha que é: ")

            if resposta != city:
                print(self.dica3)
                resposta = input("Que cidade voce acha que é: ")

            if resposta != city:
                print(self.dica4)
                resposta = input("Que cidade voce acha que é: ")

            if resposta != city:
                print(self.dica5)
                resposta = input("Que cidade voce acha que é: ")

            if resposta != city:
                print("-----Suas chances acabaram!!!!----")

            if resposta == city:
                print("------Parabéns voce acertou a palavra!!!!!!-------")


        if city == "Londres":
            self.Londres()
            print(self.dica1)
            resposta = input("Que cidade voce acha que é: ")
            if resposta != city:
                print(self.dica2)
                resposta = input("Que cidade você acha que é: ")

            if resposta != city:
                print(self.dica3)
                resposta = input("Que cidade voce acha que é: ")

            if resposta != city:
                print(self.dica4)
                resposta = input("Que cidade voce acha que é: ")

            if resposta != city:
                print(self.dica5)
                resposta = input("Que cidade voce acha que é: ")

            if resposta != city:
                print("-----Suas chances acabaram!!!!----")

            if resposta == city:
                print("------Parabéns voce acertou a palavra!!!!!!-------")


# cidades = Cidades()
# cidades.sortear_city()






