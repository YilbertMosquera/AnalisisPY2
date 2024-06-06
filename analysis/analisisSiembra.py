import pandas as pd
from data.generators.generadorAgua import generarDatosSiembra

def construirSiembrasDataFrame():
    datosSiembras=generarDatosSiembra()

    #generamos el dataframe
    residuosDataFrame = pd.DataFrame(datosSiembras,columns=['Corregimientos','Hectareassembradas','Especiessembradas','Nombre','Fecha'])

    print(residuosDataFrame)

construirSiembrasDataFrame()

