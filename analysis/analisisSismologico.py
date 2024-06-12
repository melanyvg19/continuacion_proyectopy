import pandas as pd
import matplotlib.pyplot as plt 
from data.generators.sismologico import generarDatosSismologico
from helpers.generarTabla import crearTablaHTML

def construirDTsismologico():
    datosSismologico=generarDatosSismologico()
    sismosDF=pd.DataFrame(datosSismologico, columns=['municipio','sismosUltimaAnualidad','escalaRichter','epicentro','poblacionAfectada','id'])
    sismosDF.replace('-', pd.NA,inplace=True)
    sismosDF.replace('sin',pd.NA,inplace=True)
         
    # Convertir las columnas a tipo float
    columnas_a_convertir = ['sismosUltimaAnualidad','escalaRichter','poblacionAfectada']
    sismosDF[columnas_a_convertir] = sismosDF[columnas_a_convertir].astype(float)
 
    #print(sismosDF)
    #crearTablaHTML(sismosDF,"calidadSismos")
       
    filtroSismos = sismosDF.query("(sismosUltimaAnualidad >=2)")
    #filtroRichterPeligroso = sismosDF.query("(escalaRichter >=3.5)")
    
    #Cuenta
    cuentaSismos = filtroSismos.groupby('municipio')['sismosUltimaAnualidad'].count()
    cuentaSismosDF = cuentaSismos.reset_index().rename(columns={'sismosUltimoAnio':'Sismos por Anio >=3'})
    #crearTablaHTML(cuentaSismosDF, "sismosConteoxAnio")

    #suma
    sumaSismos = filtroSismos.groupby('municipio')['sismosUltimaAnualidad'].sum()
    sumaSismosDF = sumaSismos.reset_index().rename(columns={'sismosUltimaAnualidad':'Suma de Sismos por Anio >=3'})
    #crearTablaHTML(sumaSismosDF, "sismosSumaXAnio")
            
    #Promedio
    promedioSismos = sumaSismos / cuentaSismos
    promedioSismosDF = promedioSismos.reset_index().rename(columns={'sismosUltimaAnualidad':'Promedio de Sismos por Anualidad'})
    #crearTablaHTML(promedioSismosDF, "sismosPromedio")

    tablasSismologicoDF = pd.DataFrame({
        'Cuenta Sismos': [cuentaSismosDF],
        'Suma Sismos': [sumaSismosDF],
        'Promedio Sismos': [promedioSismosDF]
    })
    crearTablaHTML(tablasSismologicoDF, "Tablas analisis simologico")
    plt.figure(figsize=(20,20))
    promedioSismos.plot(kind='bar', color='green')
    plt.title('Promedio sismos en medellin')
    plt.xlabel('Municipio')
    plt.ylabel('Evenetos sismologicos')
    plt.grid(True)
    plt.xticks(rotation=45)
    plt.savefig('./Assets/img/promedioSismos.png', format='png', dpi=300)



    
        
construirDTsismologico()


