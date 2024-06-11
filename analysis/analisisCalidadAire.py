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

    calidadAireDF.replace(['-', 'sin'], pd.NA, inplace=True)

    filtroICAPositivo=calidadAireDF.query("(ICA>20)and (ICA<50)")
    filtroICAModerado=calidadAireDF.query("(ICA>50)and (ICA<70)")
    filtroICAPeligroso=calidadAireDF.query("(ICA>=70)")
    
    cuentaPositivo = filtroICAPositivo.groupby('comuna')['ICA'].count()
    cuentaModerado = filtroICAModerado.groupby('comuna')['ICA'].count()
    cuentaPeligroso = filtroICAPeligroso.groupby('comuna')['ICA'].count()

    print("Conteo de ICA positivo por comuna:", cuentaPositivo)
    print("Conteo de ICA moderado por comuna:", cuentaModerado)
    print("Conteo de ICA peligroso por comuna:", cuentaPeligroso)

    #Suma
    sumaPositivo = filtroICAPositivo.groupby('comuna')['ICA'].sum()
    sumaModerado = filtroICAModerado.groupby('comuna')['ICA'].sum()
    sumaPeligroso = filtroICAPeligroso.groupby('comuna')['ICA'].sum()

    #Promedio
    promedioPositivo = sumaPositivo / cuentaPositivo
    promedioModerado = sumaModerado / cuentaModerado
    promedioPeligroso = sumaPeligroso / cuentaPeligroso

    promedioPositivoDF = promedioPositivo.reset_index().rename(columns={'ICA': 'Promedio ICA'})
    promedioModeradoDF = promedioModerado.reset_index().rename(columns={'ICA': 'Promedio ICA'})
    promedioPeligrosoDF = promedioPeligroso.reset_index().rename(columns={'ICA': 'Promedio ICA'})

    crearTablaHTML(promedioPositivoDF, "Calidad de aire positivo")
    crearTablaHTML(promedioModeradoDF, "Calidad de aire moderado")
    crearTablaHTML(promedioPeligrosoDF, "Calidad de aire peligroso")
    
    print("Promedio ICA Positivo por Comuna:")
    print(promedioPositivo)
    print("\nPromedio ICA Moderado por Comuna:")
    print(promedioModerado)
    print("\nPromedio ICA Peligroso por Comuna:")
    print(promedioPeligroso)
construirDataFrameCalidadAire()