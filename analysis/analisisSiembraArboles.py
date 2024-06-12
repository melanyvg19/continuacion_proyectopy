import pandas as pd
import matplotlib.pyplot as plt 
from data.generators.siembraArboles import generarSiembraArboles
from helpers.generarTabla import crearTablaHTML

def construirDTSiembraArboles():

    datosSiembraArboles=generarSiembraArboles()

    siembraArbolesDF=pd.DataFrame(datosSiembraArboles, columns=['corregimiento', 'nombre', 'id', 'hectareasSembradasAnio', 'especie'])
    crearTablaHTML(siembraArbolesDF, "TablaSiembraArboles")

    siembraArbolesDF.replace('sin', pd.NA, inplace=True)
    siembraArbolesDF.replace('-', pd.NA, inplace=True)
    siembraArbolesDF.replace('no', pd.NA, inplace=True)

    nivelBajo =siembraArbolesDF.query("(hectareasSembradasAnio <= 100)")
    nivelMedio = siembraArbolesDF.query("(hectareasSembradasAnio > 100) and (hectareasSembradasAnio <= 1000)")
    nivelAlto = siembraArbolesDF.query("(hectareasSembradasAnio > 1000)")

    promedioAnalisis= siembraArbolesDF.groupby("corregimiento")['hectareasSembradasAnio'].mean()
    plt.figure(figsize=(20,20))    
    promedioAnalisis.plot(kind='bar',color='green')
    plt.title('Siembra de arboles Valle de Aburra')
    plt.xlabel('Corregimiento')
    plt.ylabel('hectareasSembradasAnio')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('./Assets/img/analisisSiembra.png',format='png',dpi=300)

    deficit = nivelBajo.groupby('corregimiento')['hectareasSembradasAnio'].count()    
    moderado = nivelMedio.groupby('corregimiento')['hectareasSembradasAnio'].count()
    superavit = nivelAlto.groupby('corregimiento')['hectareasSembradasAnio'].count()   

    #print('Niveles bajos por corregimiento:', deficit)
    #print('Niveles medios por corregimiento:', moderado)
    #print('Niveles altos por corregimiento:', superavit)

    sumaDeficit = nivelBajo.groupby('corregimiento')['hectareasSembradasAnio'].sum()
    sumaModerado = nivelMedio.groupby('corregimiento')['hectareasSembradasAnio'].sum()
    sumaSuperavit = nivelAlto.groupby('corregimiento')['hectareasSembradasAnio'].sum()

    promedioDeficit = sumaDeficit / deficit
    promedioDeficitDF = promedioDeficit.reset_index().rename(columns={'hectareasSembradasAnio':'Promedio en Deficit'})
    crearTablaHTML(promedioDeficitDF, "promedioDeficit")    

    promedioModerado = sumaModerado / moderado
    promedioModeradoDF = promedioModerado.reset_index().rename(columns={'hectareasSembradasAnio':'Promedio Moderado'})
    crearTablaHTML(promedioModeradoDF, "promedioModerado")

    promedioSuperavit = sumaSuperavit / superavit    
    promedioSuperavitDF = promedioSuperavit.reset_index().rename(columns={'hectareasSembradasAnio':'Promedio Superavit'})
    crearTablaHTML(promedioSuperavitDF, "promedioSuperavit")

    #print('Promedio Siembra bajo por corregimiento:')
    #print(promedioDeficit)
    #print('\nPromedio Siembra moderado por corregimiento:')
    #print(promedioModerado)
    #print('\nPromedio Siembra superavit por corregimiento:')
    #print(promedioSuperavit)  

construirDTSiembraArboles()