import random

def generarSiembraArboles():
    listaDatos=[]
    for i in range(1000):
        corregimiento=random.choice(['Corregimiento Altavista','Corregimiento San Antonio de Prado','Corregimiento Santa Elena',])
        hectareas=random.randint(1,20)
        especies=random.randint(10,80)
        nombre=random.choice(['ana perez','jose jimenez','marco polo','martha lucresia','karen andrea'])
        fecha=random.choice(['2024-05-15','2024-05-16','2024-05-17',])

        encuesta=[corregimiento,hectareas,especies,nombre,fecha]

        listaDatos.append(encuesta)

    return listaDatos

print(generarSiembraArboles())