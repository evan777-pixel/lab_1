def main():
    # 1. Adds n numbers
    print("--- 1. Suma de n números ---")
    n = int(input("¿Cuántos números deseas sumar?: "))
    suma_total = 0
    for i in range(n):
        numero = float(input(f"Ingresa el número {i+1}: "))
        suma_total += numero
    print(f"El resultado de la suma es: {suma_total}\n")

    # 2. Gets the inverted numbers ex 619 -> 916
    print("--- 2. Invertir números ---")
    num_str = input("Ingresa un número para invertirlo (ej. 619): ")
    numero_invertido = num_str[::-1]
    print(f"El número invertido es: {numero_invertido}\n")

    # 3. Asks the user his name, age and profession and returns it in a custom message
    print("--- 3. Mensaje Personalizado ---")
    nombre = input("Ingresa tu nombre: ")
    edad = input("Ingresa tu edad: ")
    profesion = input("Ingresa tu profesión: ")
    print(f"Hola {nombre}, tienes {edad} años y trabajas como {profesion}. ¡Es un gusto conocerte!\n")

    # 4. Asks x numbers from a user and returns only unique values
    print("--- 4. Valores Únicos ---")
    valores = input("Ingresa varios números separados por espacios: ")
    # Convertimos la entrada en una lista, luego a un "set" para eliminar duplicados, y volvemos a lista
    numeros_lista = valores.split()
    valores_unicos = list(set(numeros_lista))
    print(f"Los valores únicos que ingresaste son: {valores_unicos}\n")

if __name__ == "__main__":
    main()