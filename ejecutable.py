from clases import Detector, Radiacion, Virus, Sanador
from typing import List


def mostrar_matriz(matriz: List[List[str]]) -> None:
    """
    Muestra la matriz de ADN en formato tabular, separada de otros elementos.
    """
    if not matriz:
        print("La matriz está vacía.")
        return

    print("\n" + "=" * 30)
    print("MATRIZ DE ADN:")
    print("=" * 30)
    print("    " + "  ".join(str(i) for i in range(len(matriz[0]))))
    for idx, fila in enumerate(matriz):
        print(f"{idx} | " + "  ".join(fila))
    print("=" * 30 + "\n")


def ingresar_matriz() -> List[List[str]]:
    """
    Solicita al usuario que ingrese una matriz de ADN.
    """
    while True:
        try:
            print("\nIngrese una matriz de ADN (6 filas de 6 bases nitrogenadas, separadas por una coma y un espacio):")
            print("Ejemplo: AGATCA, GATTCA, CAACAT, GAGCTA, ATTGCG, CTGTTC")
            entrada = input("Matriz: ").strip().upper()
            elementos = entrada.split(", ")
            if len(elementos) != 6 or not all(len(fila) == 6 for fila in elementos):
                raise ValueError("Formato incorrecto. Debe ingresar 6 filas de 6 bases nitrogenadas.")
            if not all(base in "ATCG" for fila in elementos for base in fila):
                raise ValueError("Bases no válidas. Solo se permiten A, T, C y G.")
            return [list(fila) for fila in elementos]
        except ValueError as e:
            print(f"Error: {e}")


def pedir_entero(mensaje: str, min_val: int, max_val: int) -> int:
    """
    Solicita un número entero dentro de un rango válido.
    """
    while True:
        try:
            valor = int(input(mensaje))
            if min_val <= valor <= max_val:
                return valor
            else:
                print(f"Error: El número debe estar entre {min_val} y {max_val}.")
        except ValueError:
            print("Error: Debe ingresar un número entero válido.")


def validar_base_nitrogenada() -> str:
    """
    Valida que la base nitrogenada ingresada sea A, T, C o G.
    """
    while True:
        base = input("Base nitrogenada (A/T/C/G): ").strip().upper()
        if base and base in "ATCG":
            return base
        elif not base:
            print("Error: El campo está vacío. Debe ingresar una base nitrogenada (A, T, C o G).")
        else:
            print("Error: Base inválida. Solo se permiten A, T, C y G. Intente nuevamente.")


def validar_tipo_mutacion() -> str:
    """
    Valida que el tipo de mutación sea H, V o D.
    """
    while True:
        tipo = input("Tipo de mutación (H para Horizontal, V para Vertical, D para Diagonal): ").strip().upper()
        if tipo and tipo in "HVD":
            return tipo
        elif not tipo:
            print("Error: El campo está vacío. Debe ingresar un tipo de mutación (H, V o D).")
        else:
            print("Error: Tipo inválido. Solo se permiten H, V o D. Intente nuevamente.")


def imprimir_resultado(booleano: bool, mensaje: str) -> None:
    """
    Imprime el resultado booleano y el mensaje asociado.
    """
    print(f"\nResultado booleano: {booleano}")
    print(mensaje)
