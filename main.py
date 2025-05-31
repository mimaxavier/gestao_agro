from datetime import datetime
from classes.animal import Animal

vaca = Animal(123,"vaca", 5, 15)

vaca.vacinar("Vírus da Vaca Louca", '12/5/2025')
vaca.vacinar("Virus do boi", '22/05/2025')

#vaca.alimentar("Royal", 15)

vaca.produzir_leite("28/05/2025", 50)

#vaca.verificar_abate()

#vaca.mostrar_registro(123)

vaca.alimentar("Royal", 15, "31/05/2025")