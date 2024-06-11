#Rutina para generar de forma aleatoria múltiples datos con python

import random

def generarDatosSismologico():
    listaDatos=[]
    for i in range (100):
       municipio=random.choice(['Medellin','Bello','Itagui','Envigado','Sabaneta','La Estrella','Caldas','Copacabana','Girardota','Barbosa'])
       sismosUltimoAnio=random.choice(['0','1','2','3'])
       escalaRichter=random.choice(['3.4','5.5','1.1','2.3','3.1','1.8','2.9','3.5','3.6'])
       epicentro=random.choice(['Medellin','Bello','Itagui','Envigado','Sabaneta','La Estrella','Caldas','Copacabana','Girardota','Barbosa'])
       poblacionAfectada=random.choice(['14','15','20','35','41','31','16','22','28'])
       id=random.randint(0,100)
       sismologico=[municipio,sismosUltimoAnio,escalaRichter,epicentro,poblacionAfectada,id]
       
       listaDatos.append(sismologico)
    return listaDatos
print (generarDatosSismologico())