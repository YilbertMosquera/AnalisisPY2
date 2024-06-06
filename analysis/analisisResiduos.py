import pandas as pd
from data.generators.generadorAgua import generarDatosResiduos

def construirResiduosDataFrame():
    datosResiduos=generarDatosResiduos()

    #generamos el dataframe
    residuosDataFrame = pd.DataFrame(datosResiduos,columns=['comuna','Toneladas Recogidas','Tipos de Residuos','fecha','Nombre'])

    print(residuosDataFrame)

construirResiduosDataFrame()

