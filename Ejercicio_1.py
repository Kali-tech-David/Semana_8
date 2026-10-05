import random
 
 
def recorrer(inicio, fin):
   
    if inicio == fin:
        if inicio % 3 == 0:
            return inicio
        else:
            return  None
    
    if inicio < fin:
        paso = 1
    else:
        paso = -1

    resto = recorrer(inicio + paso, fin)
 
    if inicio % 3 == 0:
        if resto is None:
            return inicio
        if paso == 1:
            return max(inicio, resto)
        else:
            return min(inicio, resto)
    return resto
 
 
def ejercicio1():
    inicio = int(input("Numero de inicio: "))
    fin = int(input("Numero de fin: "))
 
    resultado = recorrer(inicio, fin)
 
    if resultado is None:
        print("No hay multiplos de 3 en el recorrido.")
    elif inicio <= fin:
        print(f"Recorrido hacia adelante. Maximo multiplo de 3: {resultado}")
    else:
        print(f"Recorrido hacia atras. Minimo multiplo de 3: {resultado}")
        
    
if __name__ == "__main__":
    print("--- Ejercicio 1 ---")
    ejercicio1()