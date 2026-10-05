import random

def generar_lista(n):
    if n <= 0:
        return []
    return [random.randint(10, 99)] + generar_lista(n - 1)
 
 
def suma_multiplos_de_3(lista, i=0):
    if i == len(lista):
        return 0
    suma_resto = suma_multiplos_de_3(lista, i + 1)
    return lista[i] + suma_resto if lista[i] % 3 == 0 else suma_resto
 
 
def ejercicio2():
    cantidad = int(input("Cantidad de elementos: "))
    lista = generar_lista(cantidad)
    print("Lista generada:", lista)
    print("Suma de los multiplos de 3:", suma_multiplos_de_3(lista))
    
def main():
    print("--- Ejercicio 2 ---")
    ejercicio2()
    
main()