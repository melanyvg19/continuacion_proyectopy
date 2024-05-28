import random

def generarDatosPluviometrico():
    listaDatos=[]
    for i in range(1000):
        municipio=random.choice(['Bello', 'Envigado', 'Sabaneta', 'Itagui', 'Belen', 'Medellin'])
        lluviasXhora=random.choice(['nn'])
        lluviasXsemana=random.choice(['nn'])
        lluviasXmes=random.choice(['nn'])
        precipitacion=random.choice=(['nn'])
        pluviometrico=[municipio,lluviasXhora,lluviasXsemana,lluviasXmes,precipitacion]

        listaDatos.append(pluviometrico)

    return listaDatos
