# for num in range(1,4):
#     name = input(f"Give the name number {num}: ")
#     
    
# Lists
# Tuples
# Strings
# Files
# 
# range(5)
# [0,1,2,3,4]

print("Pesos \t Dolares \t Euro")
for pesos in range(10,101,5):
    dolares = pesos / 20
    euro = pesos / 24
    print(f"{pesos} \t {dolares} \t\t {euro:.2f}")
    
    
import hello #name of the file  hello.py
hello.printHello()

def esCuadrada(matriz):
    """Regresa True si la matriz tiene el mismo numero de renglones y de columnas"""
    numRen = len(matriz)
    numCol = len(matriz[0])
    
    for renglon in matriz: #verifica que todos los renglones tengan el mismo numero de columnas
        tam = len(renglon)
        if (tam != numCol):
            return False
    
    if (numRen == numCol):
        return True
    else:
        return False
  
def main():
    print("Exercise 1 - esCuadrada")
    res = esCuadrada([[2,3],[9,7]])
    print(res)
    