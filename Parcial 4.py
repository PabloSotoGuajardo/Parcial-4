### Pablo Soto ###

import time

def mostrar_menu():
    print("\nTOTEM AUTOATENCIÓN CAFECONLECHE")
    print("1.- Comprar entrada a Cats.")
    print("2.- Cambio de función.")
    print("3.- Mostrar stock de funciones.")
    print("4.- Salir.")
    time.sleep(3)

def comprar_entrada(compradores, stock):
    print("\n-- Comprar entrada a Cats --")
    nombre = input("Nombre del comprador: ").strip().lower()
    if nombre in compradores:
        print("Error: Comprador ya registrado.")
        return stock
    print("Seleccione función:")
    print(f"1. Cats Día Viernes ({stock['viernes']} entradas)")    
    print(f"2. Cats Día Sábado ({stock['sabado']} entradas)")
    funcion = input("Función (1 ó 2): ").strip()
    if funcion not in ('1', '2'):
        print("Error: opción de función inválida.")
        return stock
    key = 'viernes' if funcion == '1' else 'sabado'
    if stock[key] <= 0:
        print("Error: no hay stock disponible para esa función.")
        return stock
    compradores[nombre] = key
    stock[key] -= 1
    print(f"Entrada registrada en función {1 if key == 'viernes' else 2}! Stock restantes:")
    print(f"  Función 1 (Viernes): {stock['viernes']}")
    print(f"  Función 2 (Sábado): {stock['sabado']}")
    return stock

def cambio_funcion(compradores, stock):
    print("\n-- Cambio de función --")
    nombre = input("Nombre del comprador: ").strip().lower()
    if nombre not in compradores:
        print("Error: comprador no encontrado.")
        return stock
    actual = compradores[nombre]
    nueva = 'sabado' if actual == 'viernes' else 'viernes'
    print(f"Cambiar de función {1 if actual == 'viernes' else 2} a {1 if nueva == 'viernes' else 2}? (S/N): ", end="")
    resp = input().strip().lower()
    if resp not in ('s', 'si'):
        print("Cambio cancelado.")
        return stock
    if stock[nueva] <= 0:
        print("Error: no hay stock disponible en la función destino.")
        return stock
    stock[actual] += 1
    stock[nueva] -= 1
    compradores[nombre] = nueva
    print(f"Cambio exitoso. Ahora está en función {1 if nueva == 'viernes' else 2}.")
    return stock

def mostrar_stock(compradores, stock):
    vendidas = {'viernes': 0, 'sabado': 0}
    for funcion in compradores.values():
        vendidas[funcion] += 1
    print("\n-- Stock de Funciones --")
    print(f"Función 1 (Viernes): Disponibles {stock['viernes']}, Vendidas {vendidas['viernes']}")
    print(f"Función 2 (Sábado): Disponibles {stock['sabado']}, Vendidas {vendidas['sabado']}")

def menu():
    stock = {'viernes': 150, 'sabado': 180}
    compradores = {}
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        if opcion == '1':
            time.sleep(1)  
            stock = comprar_entrada(compradores, stock)
        elif opcion == '2':
            time.sleep(1)
            stock = cambio_funcion(compradores, stock)
        elif opcion == '3':
            time.sleep(1)
            mostrar_stock(compradores, stock)
        elif opcion == '4':
            time.sleep(1)
            print("\nPrograma terminado...")
            break
        else:
            print("Debe ingresar una opción válida!!")

if __name__ == "__main__":
    menu()
