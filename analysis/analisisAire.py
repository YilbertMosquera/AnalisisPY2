import pandas as pd
from data.generators.generadorAgua import generarDatosCalidadAire
from helpers.crearTablaHTML import crearTaba

def construirAireDataFrame():
    datosAire=generarDatosCalidadAire()

    #generamos el dataframe
    aireDataFrame = pd.DataFrame(datosAire,columns=['comuna','ph','nive de oxigeno disuelto','fecha de muestreo','responsable del monitoreo'])

    #generamos el recurso HTML
    crearTaba(aireDataFrame, "DatosAire")

    print(aireDataFrame)

    aireDataFrame.replace('sin', pd.NA, inplace=True)

    print(aireDataFrame)

construirAireDataFrame()