# EJERCICIO 1

#  variables 
clima_soleado = True
presupuesto = 100000
es_sabado = True

dinero_centro_cultural = 5000
sin_trabajos = False

pelicula_cine = True
cupones_mama = True
entradas_papa = False


opcion_uno = (clima_soleado and presupuesto >= 95000) and es_sabado
opcion_dos = (dinero_centro_cultural >= 15000) and sin_trabajos
opcion_tres = pelicula_cine and (cupones_mama or entradas_papa)



# Mostrar resultados
print("--- EVALUACIÓN DE VIABILIDAD DE LA SALIDA ---")
print(f"¿Se cumple la Opción Uno?: {opcion_uno}")
print(f"¿Se cumple la Opción Dos?: {opcion_dos}")
print(f"¿Se cumple la Opción Tres?: {opcion_tres}")
print(f"¿Es viable realizar alguna actividad?: {viabilidad_total}")
