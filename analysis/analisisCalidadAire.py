import pandas as pd

from data.generators.generadorCalidadAire import generarDatosCalidadAire
from helpers.generarTabla import crearTablaHTML
 
#1. PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME 

def construirDataFrameCalidadAire():
    #traigo los datos generados en el mock
    datosCalidadAire=generarDatosCalidadAire()

    #construyo el dataframe

    calidadAireDF=pd.DataFrame(datosCalidadAire, columns=['comuna', 'poblacionTotal', 'muestra', 'ICA', 'fecha', 'nombre', 'id'])

    #probando
    print(calidadAireDF)
    crearTablaHTML(calidadAireDF, "calidadAire")

construirDataFrameCalidadAire()