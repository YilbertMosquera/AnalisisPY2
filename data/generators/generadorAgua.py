import random

def generarAgua():
    listaDatos=[]
    for i in range(1000):
        comuna=random.randint(1,14)
        ph=random.randint(1,14)
        oxigeno = random.randint(1,9)
        fecha=random.choice(['2024-02-15','2024-02-16','2024-02-17',])
        responsable=random.choice(["Carlos García","María Rodríguez","Juan Pérez","Ana Martínez","Luis Fernández","Elena Gómez","Miguel Sánchez",])
        encuesta=[comuna,ph,oxigeno,fecha,responsable]

        listaDatos.append(encuesta)

    return listaDatos

print(generarAgua())