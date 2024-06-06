import pandas as pd
from data.generators.generadorAgua import generarDatosCalidadAire

def construirAireDataFrame():
    datosAire=generarDatosCalidadAire()

    #generamos el dataframe
    aireDataFrame = pd.DataFrame(datosAire,columns=['comuna','ph','nive de oxigeno disuelto','fecha de muestreo','responsable del monitoreo'])

    print(aireDataFrame)

construirAireDataFrame()