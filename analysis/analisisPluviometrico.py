import pandas as pd
from data.generators.pluviometrico import generarDatosPluviometrico

def construirDTpluviometrico():
    datosPluviometrico=generarDatosPluviometrico()
    pluviometricoDF=pd.DataFrame(datosPluviometrico, columns=(['municipio', 'lluviaXhora', 'lluviaXsemana', 'lluviaXmes', 'precipitacion']))
    print(pluviometricoDF)
construirDTpluviometrico()