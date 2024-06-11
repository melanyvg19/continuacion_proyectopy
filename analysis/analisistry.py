# Función para construir el DataFrame y analizar los datos
def construirDataFrameCalidadAire():
    # Traigo los datos generados en el mock
    datosCalidadAire = generarDatosCalidadAire()

    # Construyo el DataFrame
    calidadAireDF = pd.DataFrame(datosCalidadAire, columns=['comuna', 'poblacionTotal', 'muestra', 'ICA', 'fecha', 'nombre', 'id'])

    # Limpiando el DataFrame
    calidadAireDF.replace('sin', pd.NA, inplace=True)
    calidadAireDF.replace('-', pd.NA, inplace=True)
    calidadAireDF.dropna(inplace=True)

    # Convertir columnas 'poblacionTotal' y 'muestra' a tipo numérico
    calidadAireDF['poblacionTotal'] = pd.to_numeric(calidadAireDF['poblacionTotal'])
    calidadAireDF['muestra'] = pd.to_numeric(calidadAireDF['muestra'])

    # Clasificación de la calidad del aire
    def clasificarCalidadAire(ica):
        if 20 <= ica < 45:
            return 'positivo'
        elif 45 <= ica < 70:
            return 'intermedio'
        elif ica >= 70:
            return 'peligroso'
        else:
            return 'desconocido'

    calidadAireDF['nivelCalidadAire'] = calidadAireDF['ICA'].apply(clasificarCalidadAire)

    # Contar, sumar y promediar por comuna
    conteoPorComuna = calidadAireDF.groupby('comuna').size()
    sumaICAporComuna = calidadAireDF.groupby('comuna')['ICA'].sum()
    promedioICAporComuna = calidadAireDF.groupby('comuna')['ICA'].mean()

    # Resultados
    print("Conteo por comuna:")
    print(conteoPorComuna)
    print("\nSuma de ICA por comuna:")
    print(sumaICAporComuna)
    print("\nPromedio de ICA por comuna:")
    print(promedioICAporComuna)

    # Filtros por nivel de calidad del aire
    filtroPositivo = calidadAireDF.query("20 <= ICA < 45")
    filtroIntermedio = calidadAireDF.query("45 <= ICA < 70")
    filtroPeligroso = calidadAireDF.query("ICA >= 70")

    print("\nCalidad del aire positiva:")
    print(filtroPositivo)
    print("\nCalidad del aire intermedia:")
    print(filtroIntermedio)
    print("\nCalidad del aire peligrosa:")
    print(filtroPeligroso)

# Llamada a la función para construir el DataFrame y analizar los datos
construirDataFrameCalidadAire()
#
Para cumplir con los requisitos que has mencionado, podemos modificar y ampliar tu código para incluir las operaciones de contar, sumar y promediar los datos por comuna, y clasificar la calidad del aire en los tres niveles que has definido. Aquí tienes una versión ampliada de tu código:

python
Copiar código
import random
import pandas as pd

# Función para generar datos de calidad de aire
def generarDatosCalidadAire():
    listaDatos = []
    for i in range 1000):
        comuna = random.choice(['comuna 1 popular', 'comuna 2 sta cruz', 'comuna 12 la america', 'comuna 4 aranjuez','comuna 5 castilla','comuna 6 doce de octubre', 'comuna 7 robledo','comuna 8 villa hermosa', 'comuna 9 buenos aires', 'comuna 10 la canelaria', 'comuna 11 laureles','comuna 12', 'comuna 13 san javier','comuna 14 el poblado','comuna 15 guayabal', 'comuna 16 belen', 'comuna 3 manrique', 'sin', '-'])
        totalPoblacion = random.choice(['3000','4500', '5000', '10000'])
        tamañoMuestra = random.choice(['1000','2000', '3500', '6000'])
        ica = random.randint(20, 100)
        fecha = random.choice(["2024-05-14","2024-05-15"])
        nombreEncuestado = random.choice(['Pedro Perez', 'Sandra Jimenez', 'Melany Valle', 'Edison Ospina', 'Isleny Gutierrez', 'Kevin Albeiro', 'Carlos Valle', 'Angi Valle', 'Estefany Valle', 'Mathias Castrillon', 'Alan Valle', 'Juan Jose Gallego', 'Keylly Paniagua', 'Gonzalo Gonzales'])
        id = random.randint(0, 1000000)
        calidadAire = [comuna, totalPoblacion, tamañoMuestra, ica, fecha, nombreEncuestado, id]

        listaDatos.append(calidadAire)
    return listaDatos

# Función para construir el DataFrame y analizar los datos
def construirDataFrameCalidadAire():
    # Traigo los datos generados en el mock
    datosCalidadAire = generarDatosCalidadAire()

    # Construyo el DataFrame
    calidadAireDF = pd.DataFrame(datosCalidadAire, columns=['comuna', 'poblacionTotal', 'muestra', 'ICA', 'fecha', 'nombre', 'id'])

    # Limpiando el DataFrame
    calidadAireDF.replace('sin', pd.NA, inplace=True)
    calidadAireDF.replace('-', pd.NA, inplace=True)
    calidadAireDF.dropna(inplace=True)

    # Convertir columnas 'poblacionTotal' y 'muestra' a tipo numérico
    calidadAireDF['poblacionTotal'] = pd.to_numeric(calidadAireDF['poblacionTotal'])
    calidadAireDF['muestra'] = pd.to_numeric(calidadAireDF['muestra'])

    # Clasificación de la calidad del aire
    def clasificarCalidadAire(ica):
        if 20 <= ica < 45:
            return 'positivo'
        elif 45 <= ica < 70:
            return 'intermedio'
        elif ica >= 70:
            return 'peligroso'
        else:
            return 'desconocido'

    calidadAireDF['nivelCalidadAire'] = calidadAireDF['ICA'].apply(clasificarCalidadAire)

    # Contar, sumar y promediar por comuna
    conteoPorComuna = calidadAireDF.groupby('comuna').size()
    sumaICAporComuna = calidadAireDF.groupby('comuna')['ICA'].sum()
    promedioICAporComuna = calidadAireDF.groupby('comuna')['ICA'].mean()

    # Resultados
    print("Conteo por comuna:")
    print(conteoPorComuna)
    print("\nSuma de ICA por comuna:")
    print(sumaICAporComuna)
    print("\nPromedio de ICA por comuna:")
    print(promedioICAporComuna)

    # Filtros por nivel de calidad del aire
    filtroPositivo = calidadAireDF.query("20 <= ICA < 45")
    filtroIntermedio = calidadAireDF.query("45 <= ICA < 70")
    filtroPeligroso = calidadAireDF.query("ICA >= 70")

    print("\nCalidad del aire positiva:")
    print(filtroPositivo)
    print("\nCalidad del aire intermedia:")
    print(filtroIntermedio)
    print("\nCalidad del aire peligrosa:")
    print(filtroPeligroso)

# Llamada a la función para construir el DataFrame y analizar los datos
construirDataFrameCalidadAire()
En este código, he añadido las siguientes funcionalidades:

Clasificación de la calidad del aire en tres niveles: positivo, intermedio y peligroso.
Conteo de registros por comuna.
Suma del ICA por comuna.
Promedio del ICA por comuna.
Además, he convertido las columnas poblacionTotal y muestra a tipo numérico para garantizar que las operaciones matemáticas se realicen correctamente. También he corregido algunos errores menores y añadido la clasificación de calidad del aire basada en el ICA.

Si necesitas realizar algún ajuste adicional o tienes más requisitos, házmelo saber.