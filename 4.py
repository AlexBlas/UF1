'''Programa diferencia 2 numeros'''
print("Escriu 2 noms")
A = int(input("N1:"))
B = int(input("N2:"))

if A > B:
    print(A, "Es mes gran que", B)

else:
    if A < B:
        print(A, "Es més petit que", B)

    else:
        if A == B:
            print(A, "Es igual que", B)
