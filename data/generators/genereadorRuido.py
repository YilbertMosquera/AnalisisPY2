import random

def generarDatosDelRuido():
    listaDatos=[]
    for i in range(1000):
        comuna=random.randint(1,14)
        direccion=random.choice(['Cr16a #29 El vergel','Cl20 #50B Buenos aires','Cr45A #45 Belen',])
        nombre=random.choice(['ana perez','jose jimenez','marco polo','martha lucresia','karen andrea'])
        desibeles=random.randint(10,80)
        correo=random.choice(['correo@correo.com','correo2@correo.com','correo3@correo.com','correo4@correo.com','correo5@correo.com'])

        encuesta=[nombre,comuna,ica,fecha,correo]

        listaDatos.append(encuesta)

    return listaDatos

print(generarDatosCalidadAire())