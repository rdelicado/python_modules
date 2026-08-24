def ft_count_recursive():
    # 1. Pedimos al usuario los dias totales
    days = int(input("Ingresa los dias: "))

    # 2. Cremos la funcion recursiva que llevara la cuenta
    def contar(dia_actual):
        # === REGLA 1: EL CASO BASE ===
        if dia_actual > days:
            print("Harvest time!")
            return
            # El return vacio detiene y cierra esta funcion

        # === REGLA 2: LA LLAMADA RECURSIVA ===
        # Imprime el dia en el que va
        print(f"Day {dia_actual}")
        # La funcion se llama a si misma pasado el dia siguiente
        contar(dia_actual + 1)

    # 3. Arrancamos la recursion pasandole el dia de inicio (Dia 1)
    contar(1)


if __name__ == "__main__":
    ft_count_recursive()
