import pandas as pd
from data.generators.ruido import generarDatosRuido
from helpers.generarTabla import crearTablaHTML
def construirDTRuido():
    datosRuido=generarDatosRuido()
    ruidoDF=pd.DataFrame(datosRuido, columns=['comuna', 'totalPoblacion','tamañoMuestra', 'deciblesNoche','deciblesDia', 'fecha', 'nombre', 'id', 'nombreEdificio'] )
    print(ruidoDF)
    crearTablaHTML(ruidoDF, "TablaRuido")
construirDTRuido()