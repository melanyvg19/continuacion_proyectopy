import random

def generarDatosSismologico():
    listaDatos=[]
    for i in range (1000):
       municipio=random.choice(['Bello', 'Envigado', 'Sabaneta', 'Itagui', 'Belen', 'Medellin'])
       sismosUltimoAnio=random.choice(['n'])
       escalaRichter=random.choice(['3.4', '5,5'])
       epicentro=random.choice(['Bello'])
       poblacionAfectada=random.choice(['14%'])
       sismologico=[municipio, sismosUltimoAnio,escalaRichter,epicentro,poblacionAfectada]
       listaDatos.append(sismologico)
    return listaDatos