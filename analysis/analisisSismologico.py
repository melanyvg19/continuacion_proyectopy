import pandas as pd
from data.generators.sismologico import generarDatosSismologico

def construirDTsismologico():
    datosSismologico=generarDatosSismologico()
    sismosDF=pd.DataFrame(datosSismologico, columns=['municipio', 'Sismos Del ultimo anio', 'escalaRichter', 'epicentro', 'poblacionAfectada'])
    print(sismosDF)

    construirDTsismologico()


