import pandas as pd
from data.generators.sismologico import generarDatosSismologico
from helpers.generarTabla import crearTablaHTML

def construirDTsismologico():
    datosSismologico=generarDatosSismologico()
    sismosDF=pd.DataFrame(datosSismologico, columns=['municipio', 'Sismos Del ultimo anio', 'escalaRichter', 'epicentro', 'poblacionAfectada'])
    print(sismosDF)
    crearTablaHTML(sismosDF,"TablaSismos")
construirDTsismologico()


