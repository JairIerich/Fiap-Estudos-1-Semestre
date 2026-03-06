nota1 = float(input("qual foi sua primeira nota? "))
nota2 = float(input("qual foi sua segunda nota? "))
nota3 = float(input("qual foi sua terceira nota? "))
media = (nota1 + nota2 + nota3)/3
if media >= 7:
    print(f"Aluno aprovado sua nota foi {media}")
else:
    print(f"Aluno reprovado sua nota foi {media}")
