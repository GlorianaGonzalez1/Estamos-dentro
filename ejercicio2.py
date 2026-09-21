# EJERCICIO 2


# variables 
promedio_general = 85
nota_materia_1 = 80
nota_materia_2 = 85
nota_materia_3 = 90
nota_materia_4 = 78

lavados_padre = 7
lavados_madre = 4

# Condición 1: Rendimiento Académico
# Promedio mínimo de 75 y todas las materias aprobadas con nota >= 70
rendimiento_academico = (promedio_general >= 75) and \
                         (nota_materia_1 >= 70) and \
                         (nota_materia_2 >= 70) and \
                         (nota_materia_3 >= 70) and \
                         (nota_materia_4 >= 70)

# Condición 2: Colaboración en el Hogar
# Registrar al menos 6 lavados al padre, 10 a la madre, o un total combinado de al menos 14
colaboracion_hogar = (lavados_padre >= 6) or \
                     (lavados_madre >= 10) or \
                     ((lavados_padre + lavados_madre) >= 14)

# Expresión booleana final: Debe cumplir SIMULTÁNEAMENTE ambas condiciones
premio_otorgado = rendimiento_academico and colaboracion_hogar

# Mostrar resultados
print("--- EVALUACIÓN DEL PREMIO POR ESFUERZO ---")
print(f"¿Cumple con el rendimiento académico?: {rendimiento_academico}")
print(f"¿Cumple con la colaboración en el hogar?: {colaboracion_hogar}")
print(f"¿Se le compra la consola de videojuegos a Andrés?: {premio_otorgado}")
