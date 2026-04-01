numero = int(input("qual seu numero: "))

if numero %2 == 0 and numero < 100:
    print("é divisivel e é menor q 100")
if numero %2 == 0 and numero >= 100:
    print("é divisivel e é maior q 100")
if numero %2 == 1 and numero < 100:
    print("é indivisivel e é menor q 100")
if numero %2 == 1 and numero >= 100:
    print("é indivisivel e é maior q 100")


x = int(input("seu numero: "))


if x%2 == 0:
    if x < 100: 
        print("é par e menor q 100")
    else:
        print("é par e maior ou igual a 100")
else: 
    if x < 100:
        print("é impar e menor q 100")
    else: 
        print("é impar e maior ou igual a 100")

