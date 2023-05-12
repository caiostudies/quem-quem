import random
# def menu():
#     continuar = 1
#     while continuar:
#         continuar = int(input("0. Exit \n"
#                               "1. Begin game\n"))
#         if continuar:
#             dicas
#         else:
#             break


class Dicas:
    def __init__(self):
        ...

    # def menu():
    #     continuar = 1
    #     while continuar:
    #         continuar = int(input("0. Exit \n"
    #                               "1. Begin game\n"))
    #         if continuar:
    #             return Dicas
    #         else:
    #             break
    # menu()

    def cristiano(self):
        self.dica1 = "1.Jogador mais procurado nas redes sociais"
        self.dica2 = "2.Pessoa mais seguida do instagram"
        self.dica3 = "3.Maior artilheiro da história"
        self.dica4 = "4.Campeão da Eurocopa"
        self.dica5 =  "5.Jogador Português"

    def messi(self):
        self.dica1 = "1.Campeão da copa do mundo"
        self.dica2 = "2.Viveu grande parte da vida na Europa"
        self.dica3 = "3.Tem baixa estatura"
        self.dica4 = "4.Jogador com mais premios de melhor do mundo"
        self.dica5 = "5.Jogador argentino"

    def neymar(self):
        self.dica1 = "1.Campeão da copa das confederações"
        self.dica2 = "2.Transferencia mais cara da história"
        self.dica3 = "3.Na Europa utilizou a camisa 10 e a 11"
        self.dica4 = "4.Campeão da champions"
        self.dica5 = "5.Jogador brasileiro"

    def sortear_palavra(self):
        palavras = ["Messi", "Cristiano Ronaldo", "Neymar"]
        teste = random.choice(palavras)

        print(teste)

        if teste == palavras[0]: #MESSI
            self.messi()
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

            #if resposta1 or resposta2 or resposta3 or resposta4 or resposta5 == teste:
            #    print("------Parabéns voce acertou a palavra!!!!!!-------")

            if resposta == teste:
                print("------Parabéns voce acertou a palavra!!!!!!-------")




        if teste == "Cristiano Ronaldo": #RONALDO
            self.cristiano()
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


        if teste == "Neymar": #NEYMAR
            self.neymar()
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

# dicas = Dicas()
# dicas.sortear_palavra()
