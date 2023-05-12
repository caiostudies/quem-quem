import random
class Times:
    def __init__(self):
        ...

    def real_madrid(self):
        self.dica1 = "1.Campeão de champions"
        self.dica2 = "2.Famoso por ter grandes craques ao longo da história"
        self.dica3 = "3.Se localiza na Espanha"
        self.dica4 = "4.Maior campeão da história da champions"
        self.dica5 = "5.Sua principal cor é branco"

    def sp(self):
        self.dica1 = "1.Time Brasileiro"
        self.dica2 = "2.Três vezes campeão da libertadores"
        self.dica3 = "3.Se localiza no estado de São Paulo"
        self.dica4 = "4.Time tricolor"
        self.dica5 = "5.Teve o maior goleiro artilheiro da história"

    def flamengo(self):
        self.dica1 = "1.Já foi campeão mundial"
        self.dica2 = "2.Se localiza no Rio de Janeiro"
        self.dica3 = "3.Suas cores são vermelho e preto"
        self.dica4 = "4.Maior torcida do rio"
        self.dica5 = "5.Seu principal ídolo foi o Zico"

    def sortear_times(self):
        palavras = ["Real Madrid", "São Paulo", "Flamengo"]
        teste = random.choice(palavras)

        print(teste)

        if teste == "Real Madrid":
            self.real_madrid()
            print(self.dica1)
            resposta = input("Quem voce acha que é: ")
            if resposta != teste:
                print(self.dica2)
                resposta = input("Quem você acha que é: ")

            if resposta != teste:
                print(self.dica3)
                resposta = input("Quem voce acha que é: ")

            if resposta != teste:
                print(self.dica4)
                resposta = input("Quem voce acha que é: ")

            if resposta != teste:
                print(self.dica5)
                resposta = input("Quem voce acha que é: ")

            if resposta != teste:
                print("-----Suas chances acabaram!!!!----")

            # if resposta1 or resposta2 or resposta3 or resposta4 or resposta5 == teste:
            #    print("------Parabéns voce acertou a palavra!!!!!!-------")

            if resposta == teste:
                print("------Parabéns voce acertou a palavra!!!!!!-------")

        if teste == "São Paulo":
            self.sp()
            print(self.dica1)
            resposta = input("Quem voce acha que é6: ")
            if resposta != teste:
                print(self.dica2)
                resposta = input("Quem você acha que é5: ")

            if resposta != teste:
                print(self.dica3)
                resposta = input("Quem voce acha que é: ")

            if resposta != teste:
                print(self.dica4)
                resposta = input("Quem voce acha que é: ")

            if resposta != teste:
                print(self.dica5)
                resposta = input("Quem voce acha que é: ")

            if resposta != teste:
                print("-----Suas chances acabaram!!!!----")

            if resposta == teste:
                print("------Parabéns voce acertou a palavra!!!!!!-------")

        if teste == "Flamengo":
            self.flamengo()
            print(self.dica1)
            resposta = input("Quem voce acha que é: ")
            if resposta != teste:
                print(self.dica2)
                resposta = input("Quem você acha que é: ")

            if resposta != teste:
                print(self.dica3)
                resposta = input("Quem voce acha que é: ")

            if resposta != teste:
                print(self.dica4)
                resposta = input("Quem voce acha que é: ")

            if resposta != teste:
                print(self.dica5)
                resposta = input("Quem voce acha que é: ")

            if resposta != teste:
                print("-----Suas chances acabaram!!!!----")

            elif resposta == teste:
                print("------Parabéns voce acertou a palavra!!!!!!-------")

    #     def sorteio(self):
    #         palavras = self.cristiano(), self.messi(), self.neymar()
    #         aleatorio = random.choice(palavras)
    #         if aleatorio == self.cristiano()
    #
    # class objeto:

# times = Times()
# times.sortear_times()
