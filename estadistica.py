from eii_utils import limpiar_consola,leer_entero

edad:int=0
n:int=0
i:int=0
total:int=0
promedio:float=0

limpiar_consola()

n = leer_entero("digite la cantidad de personas")

for i in range(n):
   edad = leer_entero(f"Digite la edad {i}")
  total = total + edad

promedio = total /n
print(promedio)
