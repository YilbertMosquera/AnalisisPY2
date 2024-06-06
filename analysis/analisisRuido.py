import pandas as pd
from data.generators.generadorAgua import generarDatosSiembra

def construirSiembrasDataFrame():
    datosSiembras=generarDatosSiembra()

    #generamos el dataframe
    residuosDataFrame = pd.DataFrame(datosSiembras,columns=['comuna','Dirrecion','Nombre','Decibeliodiurnos','Decibelionocturnos'])

    print(residuosDataFrame)

construirSiembrasDataFrame()

# **** RUIDO AMBIENTAL ****
#Comuna
#Dirrecion
#Nombre
#Decibeliodiurnos
#Decibelionocturnos
