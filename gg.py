while True:
     sup = int(input("Quant. de suprimento (Kg): "))
     dia = 0
     while sup > 1:
          nsp = sup / 2
          print("Dia",dia,'=' , (round(nsp,2)))
          sup = nsp
          dia += 1