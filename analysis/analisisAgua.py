import pandas as pd
from data.generators.generadorAgua import generarDatosCalidadAgua


def construirAguaDataFrame():
    datosAire=generarDatosCalidadAgua()

    #generamos el dataframe
    aguaDataFrame = pd.DataFrame(datosAire,columns=['comuna','ph','nive de oxigeno disuelto','fecha de muestreo','responsable del monitoreo'])

    print(aguaDataFrame)

construirAguaDataFrame()