print("=== CALCULADORA BÁSICA CON VALIDACIÓN ===")

while True:
    print("\nOpciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ")
    
    if opcion == '5':
        print("¡Hasta luego!")
        break
        
    if opcion in ('1', '2', '3', '4'):
        
        try:
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
        except ValueError:
            print("❌ Error: ¡Debes ingresar un número válido! Inténtalo de nuevo.")
            continue
        
        if opcion == '1':
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcion == '2':
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opcion == '3':
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opcion == '4':
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("❌ Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")