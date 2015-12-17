'''Numero mes gran'''
print("Escriu tres numeros")
A = int(input("N1:"))
B = int(input("N2:"))
C = int(input("N3:"))
D = A
if B > D:
    D = B
if C > D:
    D = C
print(D, "es el numero mes gran")
