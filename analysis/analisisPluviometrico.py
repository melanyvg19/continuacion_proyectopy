import pandas as pd
from data.generators.pluviometrico import generarDatosPluviometrico
from helpers.generarTabla import crearTablaHTML
#from helpers.generarGrafico import crearGraficoHTML

def construirDataFramepluviometrico():
    datosPluviometrico=generarDatosPluviometrico()
    pluviometricoDF=pd.DataFrame(datosPluviometrico, columns=(['municipio','lluviaXdia','lluviaXsemana','lluviaXmes','precipitacion','id']))
    pluviometricoDF.replace('-', pd.NA,inplace=True)
    pluviometricoDF.replace('sin',pd.NA,inplace=True)
    
    # Convertir las columnas a tipo float
    columnas_a_convertir = ['lluviaXdia', 'lluviaXsemana', 'lluviaXmes', 'precipitacion']
    pluviometricoDF[columnas_a_convertir] = pluviometricoDF[columnas_a_convertir].astype(float)
    
    #print(pluviometricoDF)
    #crearTablaHTML(pluviometricoDF,"calidadPluviometrico")
    
    filtroDiaPeligroso = pluviometricoDF.query("(lluviaXdia >= 5.3)")
    filtroMesPeligroso = pluviometricoDF.query("(lluviaXmes >=150)")
    filtroAnoPeligroso = pluviometricoDF.query("(precipitacion >=1900)")
    
    cuentaDiaPeligroso = filtroDiaPeligroso.groupby('municipio')['lluviaXdia'].count()
    cuentaDiaPeligrosoDF = cuentaDiaPeligroso.reset_index().rename(columns={'lluviaXdia':'llovias por dia'})
    crearTablaHTML(cuentaDiaPeligrosoDF, "comteoLluviaxDiaPeligroso")
    
    cuentaMesPeligroso = filtroMesPeligroso.groupby('municipio')['lluviaXmes'].count()
    #print("Conteo LLuvias por dia en estado Peligroso: ",cuentaMesPeligroso)
    cuentaMesPeligrosoDF = cuentaMesPeligroso.reset_index().rename(columns={'lluviaXmes':'llovias por mes'})
    crearTablaHTML(cuentaMesPeligrosoDF, "comteoLluviaxMesPeligroso")
        
    cuentaAnoPeligroso = filtroAnoPeligroso.groupby('municipio')['precipitacion'].count()
    #print("Conteo LLuvias por Ano en estado Peligroso: ",cuentaAnoPeligroso)
    cuentaAnoPeligrosoDF = cuentaAnoPeligroso.reset_index().rename(columns={'precipitacion':'llovias por Ano'})
    crearTablaHTML(cuentaAnoPeligrosoDF, "comteoLluviaxAnoPeligroso")

construirDataFramepluviometrico()















'''     # Crear el gráfico de barras
    plt.figure(figsize=(10, 6))
    cuentaDiaPeligrosoDF.plot(kind='bar', x='municipio', y='llovias por dia', color='skyblue', legend=False)
    plt.title('Cantidad de Municipios con niveles superiores de 5.3 mm por día')
    plt.xlabel('Municipio')
    plt.ylabel('Cantidad de días peligrosos')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('./static/grafico_comteoLluviaxDiaPeligroso.png')
    plt.close()
    crearGraficoHTML(cuentaDiaPeligrosoDF, "graficoCuentaDiaPeligroso")
'''

''' 
    #suma
    sumaDiaPeligroso = filtroDiaPeligroso.groupby('municipio')['lluviaXdia'].sum()
    print("Conteo LLuvias por dia en estado Peligroso: ",cuentaDiaPeligroso)
    sumaDiaPeligrosoDF = sumaDiaPeligroso.reset_index().rename(columns={'lluviaXdia':'llovias por dia'})
    crearTablaHTML(sumaDiaPeligrosoDF, "sumaLluviaxDiaPeligroso")
    
    sumaMesPeligroso = filtroMesPeligroso.groupby('municipio')['lluviaXmes'].sum()
    print("Conteo LLuvias por dia en estado Peligroso: ",cuentaMesPeligroso)
    sumaMesPeligrosoDF = sumaMesPeligroso.reset_index().rename(columns={'lluviaXmes':'llovias por mes'})
    crearTablaHTML(sumaMesPeligrosoDF, "sumaLluviaxMesPeligroso")
    
    sumaAnoPeligroso = filtroAnoPeligroso.groupby('municipio')['precipitacion'].sum()
    print("Conteo LLuvias por Ano en estado Peligroso: ",cuentaAnoPeligroso)
    sumaAnoPeligrosoDF = sumaAnoPeligroso.reset_index().rename(columns={'precipitacion':'llovias por Ano'})
    crearTablaHTML(sumaAnoPeligrosoDF, "sumaLluviaxAnoPeligroso")
    
    #Promedio
    promedioDiaPeligroso = sumaDiaPeligroso / cuentaDiaPeligroso
    print("promedio LLuvias por dia en estado Peligroso: ",promedioDiaPeligroso)
    promedioDiaPeligrosoDF = promedioDiaPeligroso.reset_index().rename(columns={'lluviaXdia':'llovias por dia'})
    crearTablaHTML(promedioDiaPeligrosoDF, "promedioLluviaxDiaPeligroso")
    
    promedioMesPeligroso = sumaMesPeligroso / cuentaMesPeligroso
    print("promedio LLuvias por dia en estado Peligroso: ",promedioMesPeligroso)
    promedioMesPeligrosoDF = promedioMesPeligroso.reset_index().rename(columns={'lluviaXmes':'pllovias por mes'})
    crearTablaHTML(promedioMesPeligrosoDF, "promedioLluviaxMesPeligroso")
    
    promedioAnoPeligroso = sumaAnoPeligroso / cuentaAnoPeligroso
    print("promedio LLuvias por Ano en estado Peligroso: ",promedioAnoPeligroso)
    promedioAnoPeligrosoDF = promedioAnoPeligroso.reset_index().rename(columns={'precipitacion':'llovias por Ano'})
    crearTablaHTML(promedioAnoPeligrosoDF, "promedioLluviaxAnoPeligroso")
 '''  