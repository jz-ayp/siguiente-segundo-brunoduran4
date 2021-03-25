"""
Inserta el encabezado aquí y escribe tu código abajo
"""

# Entradas
h=int(input("Dame horas: "))
m=int(input("Dame minutos: "))
s=int(input("Dame segundos: "))

# Proceso
if m  == 59 :
    m = 0
    h +=1
if s == 59:
    s = 0
if s  < 59:   
    s += 1


# Salidas
print("Horas", h)
print("Minutos", m)
print("Segundos", s)
