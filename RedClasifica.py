urgencia = ["paro", "bus", "metro"]
gravedad = []
duracion = []

reclamo = str.lower(input("Ingrese su reclamo: "))


def checkUrgencia():
    data = 0
    for palabra in urgencia:
        if palabra in reclamo:
            data += 1


checkUrgencia()
