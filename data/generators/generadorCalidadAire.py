#Rutina para generar de forma aleatoria múltiples datos con python

import random

def generarDatosCalidadAire():
    listaDatos=[]
    for i in range(1000):
        comuna=random.choice(['comuna 1 popular', 'comuna 2 sta cruz', 'comuna 12 la america', 'comuna 4 aranjuez','comuna 5 castilla','comuna 6 doce de octubre', 'comuna 7 robledo','comuna 8 villa hermosa', 'comuna 9 buenos aires', 'comuna 10 la canelaria', 'comuna 11 laureles','comuna 12', 'comuna 13 san javier','comuna 14 el poblado','comuna 15 guayabal', 'comuna 16 belen', 'comuna 3 manrique'])
        totalPoblacion=random.choice(['3000','4500', '5000', '10000'])
        tamañoMuestra=random.choice(['1000','2000', '3500', '6000'])
        ica=random.randint(20, 100)
        fecha=random.choice(["2024-05-14","2024-05-15"])
        nombreEncuestado=random.choice(['Pedro Perez', 'Sandra Jimenez', 'Melany Valle', 'Edison Ospina', 'Isleny Gutierrez', 'Kevin Albeiro', 'Carlos Valle', 'Angi Valle', 'Estefany Valle', 'Mathias Castrillon', 'Alan Valle', 'Juan Jose Gallego', 'Keylly Paniagua', 'Gonzalo Gonzales'])
        id=random.randint(0,1000000)
        calidadAire=[comuna,totalPoblacion,tamañoMuestra,ica,fecha,nombreEncuestado,id]

        listaDatos.append(calidadAire)
    return listaDatos

print (generarDatosCalidadAire())