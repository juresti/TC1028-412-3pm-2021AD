def calcularPromedio(cuantas):
    suma = 0
    for numMat in range(1,cuantas + 1):
        cal = int(input(f"Dime la calificacion de la materia {numMat}: "))
        suma += cal
    promedio = suma / cuantas
    return promedio

def main():
    print("Programa que calcula el promedio de tus materias")
    num = int(input("Dime cuantas materias tienes este semestre: "))
    promedio = calcularPromedio(num)
    print(f"El promedioi de tus {num} materias es de {promedio}")
    
def crearLinea(ancho):
    linea = "" #string vacio
    for veces in range(ancho):
        linea += "*"
    return linea

def main2():
    print("Programa que crea una linea del ancho indicado")
    wide = int(input("Dime el ancho de la linea: "))
    miLinea = crearLinea(wide)
    print(miLinea)
    
    
def creaCubo(ancho, alto):
    cubo = ""
    for veces in range(alto):
        cubo += crearLinea(ancho) + "\n"
    return cubo

def main3():
    print("Programa que hace un cubo del ancho y alto solicitado")
    wide = int(input("Dime el ancho: "))
    height = int(input("Dime el alto: "))
    miCubo = creaCubo(wide,height)
    print(miCubo)

def crearLineaEspaciada(ancho):
    linea = "*"
    for veces in range(ancho - 2):
        linea += " "
    linea += "*"
    return linea

    
