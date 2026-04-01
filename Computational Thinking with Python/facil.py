print("oi")
velocidade = int(input("seu velocidade: "))
multa = 0
if velocidade > 110:
    velocidaderesidual = velocidade - 110
    valormulta= velocidaderesidual * 5

    print(f"multa de 5 real aplicada, sua multa atual é de {valormulta}")

opcao = input("como deseja pagar? ")
match opcao: 

    case "credito":
        valorresidual = valormulta * 0.1
        valorcredito = valorresidual + valormulta
        print(f"paganndo no credito vc paga {valorcredito}")
        print("tchau")
    case "pix":
        valorsobra = valormulta * 0.15 
        valorpix = valormulta - valorsobra
        print(f"pagando no pix voce paga {valorpix}")
        print("tchau")


