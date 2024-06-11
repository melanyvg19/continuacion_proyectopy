import pandas as pd
from data.generators.ruido import generarDatosRuido
from helpers.generarTabla import crearTablaHTML
def construirDTRuido():
    datosRuido=generarDatosRuido()
    ruidoDF=pd.DataFrame(datosRuido, columns=['Fecha','Comuna', 'Total Poblacion','Tamaño Muestra', 'DeciblesNoche','DeciblesDía', 'Nombre', 'Id', 'Nombre Edificio'] )
    crearTablaHTML(ruidoDF, "Tabla de Ruido")

    ruidoDF.replace('sin', pd.NA, inplace=True)
    ruidoDF.replace('-', pd.NA, inplace=True)
    ruidoDF.replace('no', pd.NA, inplace=True)
    ruidoDF.dropna(inplace=True)


    #Filtros
    #Noche
    filtroNocheDbBajo=ruidoDF.query("(decibelesNoche >-100 and decibelesNoche <0)")
    filtroNocheDbMedio=ruidoDF.query("(decibelesNoche >0 and decibelesNoche <20)")
    filtroNocheDbAlto=ruidoDF.query("(decibelesNoche >-20")

    conteoValoresNocheDbBajo = filtroNocheDbBajo.groupby('Comuna')['decibelesNoche'].count()
    conteoValoresNocheDbMedio = filtroNocheDbMedio.groupby('Comuna')['decibelesNoche'].count()
    conteoValoresNocheDbAlto = filtroNocheDbAlto.groupby('Comuna')['decibelesNoche'].count()

    print('Niveles bajos por comuna(Noche):', conteoValoresNocheDbBajo)
    print('Niveles medios por comuna(Noche):', conteoValoresNocheDbMedio)
    print('Niveles altos por comuna(Noche):', conteoValoresNocheDbAlto)

    sumNocheBajo=filtroNocheDbBajo.groupby('Comuna')['decibelesNoche'].sum()
    sumNocheMedio=filtroNocheDbMedio.groupby('Comuna')['decibelesNoche'].sum()
    sumNocheAlto= filtroNocheDbAlto.groupby('Comuna')['decibelesNoche'].sum()

    promNocheBajo=sumNocheBajo/conteoValoresNocheDbBajo
    promNocheMedio=sumNocheMedio/conteoValoresNocheDbMedio
    promNocheAlto=sumNocheAlto/conteoValoresNocheDbAlto

    print('Promedio DB bajo(noche) por comuna:')
    print(promNocheBajo)
    print('\nPromedio DB medio(noche) por comuna:')
    print(promNocheMedio)
    print('\nPromedio DB alto(noche) por comuna:')
    print(promNocheAlto)

    #Dia
    filtroDiaDbBajo=ruidoDF.query("(decibelesDia >-100 and decibelesDia <0)")
    filtroDiaDbMedio=ruidoDF.query("(decibelesDia >0 and decibelesDia <20)")
    filtroDiaDbAlto=ruidoDF.query("(decibelesDia >20)")

    conteoValoresDiaDbBajo = filtroDiaDbBajo.groupby('Comuna')['decibelesDia'].count()
    conteoValoresDiaDbMedio = filtroDiaDbMedio.groupby('Comuna')['decibelesDia'].count()
    conteoValoresDiaDbAlto = filtroDiaDbAlto.groupby('Comuna')['decibelesDia'].count()

    print('Niveles bajos por comuna(Dia):', conteoValoresDiaDbBajo)
    print('Niveles medios por comuna(Dia):', conteoValoresDiaDbMedio)
    print('Niveles altos por comuna(Dia):', conteoValoresDiaDbAlto)

    sumDiaBajo=filtroDiaDbBajo.groupby('Comuna')['decibelesDia'].sum()
    sumDiaMedio=filtroDiaDbMedio.groupby('Comuna')['decibelesDia'].sum()
    sumDiaAlto=filtroDiaDbAlto.groupby('Comuna')['decibelesDia'].sum()

    promDiaBajo=sumDiaBajo/conteoValoresDiaDbBajo
    promDiaMedio=sumDiaMedio/conteoValoresDiaDbMedio
    promDiaAlto=sumDiaAlto/conteoValoresDiaDbAlto

    print('Promedio DB bajo(dia) por comuna:')
    print(promDiaBajo)
    print('\nPromedio DB medio(dia) por comuna:')
    print(promDiaMedio)
    print('\nPromedio DB alto(dia) por comuna:')
    print(promDiaAlto)

    #Tablas
    #Noche
    crearTablaHTML(promNocheBajo, "Promedio Ruido Bajo por Comuna (Noche)")
    crearTablaHTML(promNocheMedio, "Promedio Ruido Medio por Comuna (Noche)")
    crearTablaHTML(promNocheAlto, "Promedio Ruido Alto por Comuna (Noche)")

    #Dia
    crearTablaHTML(promDiaBajo, "Promedio Ruido Bajo por Comuna (Dia)")
    crearTablaHTML(promDiaMedio, "Promedio Ruido Medio por Comuna (Dia)")
    crearTablaHTML(promDiaAlto, "Promedio Ruido Alto por Comuna (Dia)")



construirDTRuido()