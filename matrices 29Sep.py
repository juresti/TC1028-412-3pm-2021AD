def crearMatriz(numRen,numCol,valor):
    matriz = []
    for ren in range(numRen):
        renglon = []
        for col in range(numCol):
            renglon.append(valor)
        matriz.append(renglon)
    
    return matriz

def imprimirMatriz(matriz):
    """Recibe una matriz y la imprime de forma que un humano la pueda leer facilmente"""
    salida = ""
    for renglon in matriz:
        for dato in renglon:
            salida += str(dato) + " "
        salida += "\n"
    
    print(salida)
    

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
    
def tamanoMatriz(matriz):
    numRen = len(matriz)
    numCol = len(matriz[0])
    
    for renglon in matriz: #verifica que todos los renglones tengan el mismo numero de columnas
        tam = len(renglon)
        if (tam != numCol):
            return -1,-1
        
    return numRen,numCol
    