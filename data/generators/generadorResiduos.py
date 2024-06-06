import random

def generarResiduos():
    listaDatos=[]
    for i in range(1000):
        comuna=random.randint(1,14)
        toneladas=random.randint(1,20)
        tiposderesiduo = random.choice(["Papel y cartón","Plástico","Vidrio","Metal","Orgánico","Electrónico","Peligroso",])
        nombre=random.choice(['ana perez','jose jimenez','marco polo','martha lucresia','karen andrea'])
        fecha=random.choice(['2024-05-15','2024-05-16','2024-05-17',])

        encuesta=[comuna,toneladas,tiposderesiduo,nombre,fecha]

        listaDatos.append(encuesta)

    return listaDatos

print(generarResiduos())