def dh_parameters():
    # Solicitar el número de grados de libertad (GDL) del robot
    grados_de_libertad = int(input("Ingrese el número de grados de libertad del robot: "))

    # Iterar sobre cada eslabón del robot
    for i in range(grados_de_libertad):
        print(f"\nConfigurando el eslabón {i + 1}:")

        # Mostrar las descripciones textuales de los parámetros DH
        print(
            f"Obtener θ_{i + 1} como el ángulo que hay que girar {{S{i}}} en torno al z_{i} para que x_{i} y x_{i + 1} queden paralelos.")
        print(
            f"Obtener d_{i + 1} como la distancia que habría que desplazar {{S{i}}} para que x_{i} y x_{i + 1} quedasen alineados, medida a lo largo de z_{i}.")
        print(
            f"Obtener a_{i + 1} como la distancia medida a lo largo de x_{i} (que ahora coincidiría con x_{i + 1}) que habría que desplazar el nuevo {{S{i}}} para que su origen coincidiese con {{S{i + 1}}}.")
        print(
            f"Obtener α_{i + 1} como el ángulo que habría que girar {{S{i}}} en torno a x_{i} (que ahora coincidiría con x_{i + 1}) para que el nuevo {{S{i}}} coincidiese totalmente con {{S{i + 1}}}.")

        # Solicitar valores para cada parámetro
        theta = input(f"\nIngrese el valor de θ_{i + 1} (en grados): ")
        d = input(f"Ingrese el valor de d_{i + 1}: ")
        a = input(f"Ingrese el valor de a_{i + 1}: ")
        alpha = input(f"Ingrese el valor de α_{i + 1} (en grados): ")

        # Mostrar un resumen de los valores ingresados
        print(f"\nValores para el eslabón {i + 1}:")
        print(f"θ_{i + 1} = {theta} grados")
        print(f"d_{i + 1} = {d}")
        print(f"a_{i + 1} = {a}")
        print(f"α_{i + 1} = {alpha} grados")

        # Presionar Enter para continuar al siguiente eslabón
        input("\nPresiona Enter para pasar al siguiente eslabón...")

    print("\nTodos los parámetros DH han sido configurados correctamente.")


# Llamada a la función
dh_parameters()
