from datetime import date, timedelta

def calcular_y_para_fecha(fecha_a_evaluar: date, fecha_base_referencia: date, desfase_inicial: int = 0) -> int:
    """
    Calcula el valor de 'y' (0-9) para una fecha dada,
    basándose en una fecha de referencia y un desfase inicial.
    'y' incrementa en 1 cada día y cicla de 0 a 9.
    """
    # Calcular la diferencia en días desde la fecha de referencia hasta la fecha a evaluar
    diferencia_dias = (fecha_a_evaluar - fecha_base_referencia).days

    # Aplicar el desfase inicial y luego el módulo 10 para asegurar el ciclo 0-9
    # Si desfase_inicial es 0, el primer día (diferencia 0) da 0 % 10 = 0
    # Si desfase_inicial es 1, el primer día (diferencia 0) da (0 + 1) % 10 = 1
    y = (diferencia_dias + desfase_inicial) % 10

    return y

def main():
    print("===========================================")
    print("  VALORES DIARIOS DE 'Y' PARA ADIF")
    print("===========================================")

    # Definir la fecha base de referencia tal como se indicó
    # El 24 de mayo de 2025, 'y' para pares es 0 y para impares es 1
    FECHA_BASE = date(2025, 5, 24)

    while True:
        print("\nIntroduce la fecha que deseas evaluar (formato AAAA-MM-DD), o escribe 'salir' para terminar:")
        fecha_str = input("Fecha: ")

        if fecha_str.lower() == 'salir':
            break

        try:
            # Intentar convertir la entrada del usuario a un objeto date
            anio, mes, dia = map(int, fecha_str.split('-'))
            fecha_evaluar = date(anio, mes, dia)
        except ValueError:
            print("ERROR: Formato de fecha incorrecto. Por favor, usa AAAA-MM-DD.")
            continue # Volver a pedir la fecha

        print(f"\n--- Resultados para la fecha: {fecha_evaluar.strftime('%d/%m/%Y')} ---")

        # Calcular 'y' para la referencia de los Pares
        # Comienza en 0 en la FECHA_BASE
        y_pares = calcular_y_para_fecha(fecha_evaluar, FECHA_BASE, desfase_inicial=0)
        print(f"Para la referencia de 93 PARES, el valor de 'y' es: {y_pares}")

        # Calcular 'y' para la referencia de los Impares
        # Comienza en 1 en la FECHA_BASE
        y_impares = calcular_y_para_fecha(fecha_evaluar, FECHA_BASE, desfase_inicial=1)
        print(f"Para la referencia de 93 IMPARES, el valor de 'y' es: {y_impares}")

    print("\nPrograma finalizado. ¡Hasta luego!")

if __name__ == "__main__":
    main()
