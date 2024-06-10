import random

def generarDatosRuido():
    listaDatos=[]
    for i in range (1000):
        comuna=random.choice(['Comuna 1 Popular', 'Comuna 2 Santa Cruz', 'Comuna 12 la america', 'Comuna 4 Aranjuez','Comuna 5 Castilla','Comuna 6 Doce de Octubre', 'Comuna 7 Robledo','Comuna 8 Villa Hermosa', 'Comuna 9 Buenos Aires', 'Comuna 10 La Canelaria', 'Comuna 11 Laureles','Comuna 12 La América', 'Comuna 13 San Javier','Comuna 14 El Poblado','Comuna 15 Guayabal', 'Comuna 16 Belén', 'Comuna 3 Manrique'])
        totalPoblacion=random.choice(['3000','4000','5000','6000','7000','8000','9000','10000','11000','12000','13000','14000','15000','16000','17000','18000'])
        tamañoMuestra=random.choice(['500','1000','1500','2000','2500','3000','3500','4000','4500','5000','5500','6000','6500','7000','7500','8000'])
        decibelesNoche=random.choice(['10', '24', '44', '43', '98','-5','-15','-8','-2','5','53','4','-20','32','6'])
        decibelesDia=random.choice(['-10', '64', '44', '43', '98','-8','-30','50','76'])
        fecha=random.choice(["2023-05-14","2024-05-14","2023-12-21","2024-12-07","2023-03-28","2023-08-25","2024-03-05","2024-08-23"])
        nombreEncuestado=random.choice(['Vicent Francisco','Azucena Sanchez','Jose Felix Herraiz','Maria Amores','Manuel Antonio Paz','Paloma Solana','Jose Gabriel Mir','Miren Ochoa','Francisco Miguel Contreras','Ursula Sans','Ernesto Estrada','Brigida Vilchez','Rufino Giron','Maria Jose Vega','Jose Pablo Cervantes','Daniela Gabarri','Jose Ignacio Campos'])
        id=random.randint(0,1000000)
        nombreEdificio=random.choice(['Coltejer', 'Comfama', 'Coltabaco', 'Espejos', 'Atlas', 'Gran Colombia','Cerezos','Doña Ana','Continental','Sucre','Parra','San Vicente','Archid','DaVinci','La enmienda','Los Colores','sin','no','-'])
        datosRuido=[comuna,totalPoblacion,tamañoMuestra,decibelesDia,decibelesNoche,fecha,nombreEdificio,nombreEncuestado,id]
        listaDatos.append(datosRuido)
    return listaDatos