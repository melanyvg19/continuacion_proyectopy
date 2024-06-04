import pandas as pd
from data.generators.pluviometrico import generarDatosPluviometrico
from helpers.generarTabla import crearTablaHTML

def construirDTpluviometrico():
    datosPluviometrico=generarDatosPluviometrico()
    pluviometricoDF=pd.DataFrame(datosPluviometrico, columns=(['municipio', 'lluviaXhora', 'lluviaXsemana', 'lluviaXmes', 'precipitacion']))
    print(pluviometricoDF)
    crearTablaHTML(pluviometricoDF, "TablaPluviometrico")
construirDTpluviometrico()