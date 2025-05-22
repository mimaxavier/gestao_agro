from datetime import datetime
from classes.animal import Animal

vaca = Animal(123,"vaca", 5)

vaca.vacinar("Vírus da Vaca Louca", '12/5/2025')
vaca.vacinar("Virus do boi", '22/05/2025')

vaca.alimentar()

vaca.produzir_leite()

vaca.verificar_abate()

vaca.mostrar_registro(123)