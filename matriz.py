def creaMatriz(n,m):
 '''
 Esta función crea una matríz vacía con n filas y n columnas.
 @param n : Número de filas.
 @param m : Número de columnas
 @type n: int
 @type m: int
 @return: devuelve una matriz n por m
 @rtype: matriz (lista de listas)
 '''
 matriz = []
 for i in range(n):
    a = [0]*m
    matriz.append(a)
 return matriz

def Mostrar(fras,tweets):
    contF = 0
    contTweets = 1
    print("Total de tweets = ", tweets)
    print("La matriz es la siguiente:")
    while contTweets <= tweets:
        print("\t", "tw",contTweets,end=" ")
        contTweets += 1
        
    print("")
    for fila in matriz:
        print(fras[contF])
        contF += 1
        for valor in fila:
            print("\t", valor, end=" ")
        print()

#nombre del archivo de texto
archivo = 'Test2.txt'

#Aqui se agrega la frase a buscar
frase = ["algo", "que", "noche", "gracias","no"]

#Se asignan las dimenciones de la matriz
filaM = len(frase)
with open(archivo) as myfile:
    total_lines = sum(1 for line in myfile)
columnaM = total_lines
#print(filaM)
#print(columnaM)

#inicializamos variables y matriz
#print(frase[0])
cont = 0
indiceColumna = 0
matriz = creaMatriz(filaM,columnaM)

with open(archivo,"r") as archivo:
    for linea in archivo:
        palabras = linea.split()
        contF = 0
        value = 0
        for fila in frase:
            contP = 0
            for columna in palabras:
                value = 0
                if(frase[contF] == palabras[contP]):
                    #print("true")
                    value = 1
                    
                contP += 1
                if(bool(value)):
                    matriz[contF][indiceColumna] = 1
            value = 0    
            contF += 1
        indiceColumna += 1
    Mostrar(frase,total_lines)
