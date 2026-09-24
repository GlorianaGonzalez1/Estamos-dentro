from eii_utils import limpiar_consola, leer_flotante

kWh:float=0.00
alumbrado:float=0.00
tributo:float=0.00
iva:float=0.00
tarifa:float=0.00
total:float=0.00

limpiar_consola()
kWh=leer_flotante("Ingrese la cantidad de kilovatios-hora consumidos en el mes")
if (kWh>30):
   if (kWh>200):
      if (kWh>300):
         tarifa=1744.80+9887.20+8924.00+92.27*(kWh-300)
      else:
         tarifa=1744.80+9887.20+89.24*(kWh-200)
   else:
      tarifa=1744.80+58.16*(kWh-30)
else:
   tarifa=1744.80
alumbrado=kWh*3.02
if kWh<=100:
   tributo=0.00
elif kWh<=21750:
   tributo=0.0175*tarifa
else:
   tributo=154347.50*0.0175

if kWh<=280:
   iva=0.00
else: 
   iva=0.13*(tarifa+alumbrado+tributo)
total=tarifa+alumbrado+tributo+iva

print(f"-"*40)
print(f"-"*40)
print(f"DESGLOCE DE FACTURA ELƒCTRICA (CNFL)")
print(f"-"*40)
print(f"Consumo mensual: {kWh} kWh")
print(f"Subtotal energ’a: {tarifa:.2f}")
print(f"Alumbrado pœblico: {alumbrado:.2f}")
print(f"Tributo: {tributo:.2f}")
print(f"IVA: {iva:.2f}")
print(f"Total: {total:.2f}")
print(f"-"*40)
print(f"TOTAL A PAGAR: ?{total:.2f}")
print(f"-"*40)
print(f"-"*40)
