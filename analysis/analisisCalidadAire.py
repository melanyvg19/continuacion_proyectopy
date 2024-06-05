import pandas as pd

from data.generators.generadorCalidadAire import generarDatosCalidadAire
from helpers.generarTabla import crearTablaHTML
 
#1. PARA ANALIZAR DATOS CON PYTHON DEBEMOS CONSTRUIR UN DATAFRAME 

def construirDataFrameCalidadAire():
    #traigo los datos generados en el mock
    datosCalidadAire=generarDatosCalidadAire()

    #construyo el dataframe

    calidadAireDF=pd.DataFrame(datosCalidadAire, columns=['comuna', 'poblacionTotal', 'muestra', 'ICA', 'fecha', 'nombre', 'id'])


    #Limpiando el dataframe

    #FORMA UNO
    #1.Limpiando (reemplazando valores)

    #calidadAireDF.replace('-', pd.NA, inplace=True)
    #calidadAireDF.replace('sin', pd.NA, inplace=True)

    #FORMA DOS
    #2.Limpiando (eliminando valores)
    calidadAireDF.replace('sin', pd.NA, inplace=True)
    calidadAireDF.dropna(inplace=True) #inplace es para que haga el cambio efectivo

    #FORMA TRES
    #filtrando datos para depurar informacion
    #filtrar datos es obtener nuevos dataframes al aplicar condiciones lógicas
    #contar datos
    #consultar datos específicos
    #filtroICAPositivo=calidadAireDF.query("(ICA>20)and (ICA<50)")  #permite aplicar condiciones lógicas al dataframe
    #filtroICAModerado=calidadAireDF.query("(ICA>50)and (ICA<70)")
    filtroICAPeligroso=calidadAireDF.query("(ICA>=70)")
    conteoValoresICAPeligroso = filtroICAPeligroso['ICA'].value_counts()
    sumaValoresICAPeligroso = conteoValoresICAPeligroso.sum()
    
    
    #probando
    print(filtroICAPeligroso)
    print("\n")
    print(conteoValoresICAPeligroso)
    print("\n")
    #print(sumaValoresICAPeligroso)
    #crearTablaHTML(calidadAireDF, "calidadAire")

construirDataFrameCalidadAire()