import random

def generarSiembraArboles():
    listaDatos=[]
    for i in range(1000):
        corregimiento=random.choice(['Altavista','San Antonio de Prado', 'San Cristobal', 'Santa Elena', 'San Sebastian de Palmitas'])
        nombre=random.choice(['Peppa Pig', 'Barney', 'Sportacous', 'Gilberto Jimenez', 'Rodolfo Hernandez', 'Gustavo Petro', 'Alvaro Uribe', 'Donald Trump', 'Cesar Gaviria', 'J Balvin', 'Nicolas Mora', 'Beatriz Pinzon', 'German Quintero'])
        id=random.randint(0,1000000)
        hectareasSembradasAño=random.randint(0,50000)
        especieSembrada=random.choice(['Samanes', 'cedros', 'chochos', 'ébanos', 'acacias amarillas y rojas', 'guayabillos', 'caobas'])
        siembraArboles=[corregimiento,nombre,id,hectareasSembradasAño,especieSembrada]
        
        listaDatos.append(siembraArboles)

    return listaDatos

