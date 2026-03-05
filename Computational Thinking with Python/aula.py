nome = input("qual seu nome?")
idade = int(input("qual sua idade?"))

if idade >= 18:
    print(f"{nome} vc é maior de idade e tem {idade} anos")
else:
    print(f"{nome} vc é menor de idade e tem {idade} anos")