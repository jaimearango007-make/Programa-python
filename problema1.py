# Problema 1: Clasificación de compromiso de sesiones de clientes

def clasificar_compromiso(duracion, clics):
    if duracion > 180 and clics > 8:
        return "Alto"
    elif duracion < 60 or clics < 3:
        return "Bajo"
    else:
        return "Medio"


sesiones = [
    ["C001", 200, 10],
    ["C002", 45, 5],
    ["C003", 120, 6],
    ["C004", 300, 2],
    ["C005", 190, 9]
]


print("INFORME DE CLASIFICACIÓN DE COMPROMISO")
print("--------------------------------------")
print("ID Cliente\tClasificación")
print("--------------------------------------")

for sesion in sesiones:
    id_cliente = sesion[0]
    duracion = sesion[1]
    clics = sesion[2]

    clasificacion = clasificar_compromiso(duracion, clics)

    print(f"{id_cliente}\t\t{clasificacion}")

print("--------------------------------------")
print("Fin del informe")
