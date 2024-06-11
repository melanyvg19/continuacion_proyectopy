#Rutina para generar de forma aleatoria múltiples datos con python
import random

def generarDatosPluviometrico():
    listaDatos=[]
    for i in range(100):
        municipio=random.choice(['Medellin:','Bello:','Itagui:','Envigado:','Sabaneta:','La Estrella:','Caldas:','Copacabana:','Girardota:','Barbosa:'])
        lluviasXdia=random.choice(['5.5','5.2','5.0','5.1','5.3','5.0','4.8','5.4','5.2','5.6'])
        lluviasXsemana=random.choice(['38.5','36.4','35.0','35.7','37.1','33.6','37.8','36.4','39.2'])
        lluviasXmes=random.choice(['165.0','156.8','150.0','153.3','159.0','150.0','144.0','162.0','156.8','169.0'])
        precipitacion=random.choice(['1980.0','1881.6','1800.0','1840.0','1908.0','1800.0','1728.0','1944.0','1881.6','2028.0'])
        id=random.randint(0,100)
        pluviometrico=[municipio,lluviasXdia,lluviasXsemana,lluviasXmes,precipitacion,id]
        
        listaDatos.append(pluviometrico)
    return listaDatos
print(generarDatosPluviometrico())