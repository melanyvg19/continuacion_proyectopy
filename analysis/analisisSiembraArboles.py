import pandas as pd
from data.generators.siembraArboles import generarSiembraArboles

def contruirDTSiembraArboles():

    datosSiembraArboles=generarSiembraArboles()

    siembraArbolesDF=pd.DataFrame(datosSiembraArboles, columns=['corregimineto', 'nombre', 'id', 'hectareascanio', 'especie'])

    print(siembraArbolesDF)

contruirDTSiembraArboles()