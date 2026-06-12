print("=== CALCULADORA BÁSICA ===")

while True:
    # Mostrar el menú de opciones
    print("\nOpciones:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")
    
    opcion = input("Seleccione una opción (1-5): ")
    
    # Validar si el usuario quiere salir del programa
    if opcion == '5':
        print("¡Hasta luego!")
        break
        
    # Validar que la opción ingresada sea correcta antes de pedir los números
    if opcion in ('1', '2', '3', '4'):
        # Solicitar los dos números para la operación
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        
        # Ejecutar la operación según la opción elegida
        if opcion == '1':
            resultado = num1 + num2
            print(f"Resultado: {num1} + {num2} = {resultado}")
            
        elif opcion == '2':
            resultado = num1 - num2
            print(f"Resultado: {num1} - {num2} = {resultado}")
            
        elif opcion == '3':
            resultado = num1 * num2
            print(f"Resultado: {num1} * {num2} = {resultado}")
            
        elif opcion == '4':
            # Validar división por cero
            if num2 != 0:
                resultado = num1 / num2
                print(f"Resultado: {num1} / {num2} = {resultado}")
            else:
                print("Error: No se puede dividir entre cero.")
    else:
        print("Opción no válida. Por favor, intente de nuevo.")