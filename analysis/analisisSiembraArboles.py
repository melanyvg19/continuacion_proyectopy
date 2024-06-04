import pandas as pd
from data.generators.siembraArboles import generarSiembraArboles
from helpers.generarTabla import crearTablaHTML

def contruirDTSiembraArboles():

    datosSiembraArboles=generarSiembraArboles()

    siembraArbolesDF=pd.DataFrame(datosSiembraArboles, columns=['corregimineto', 'nombre', 'id', 'hectareascanio', 'especie'])

    print(siembraArbolesDF)
    crearTablaHTML(siembraArbolesDF, "TablaSiembraArboles")

contruirDTSiembraArboles()