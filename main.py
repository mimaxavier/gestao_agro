from datetime import datetime
from models.animal import Animal
from models.plantation import Plantation
from models.vaccine import VaccineApplication

dolomita = Animal(1, "cow", "26/09/2025", 250.57)

#dolomita.vacinar("Raiva", "23/02/2026")

#dolomita.obter_historico("Vacinação")

dolomita.vacinar("Brucelose", "20/04/2025")
dolomita.vacinar("Raiva", "21/03/2025")

dolomita.obter_historico("Vacinação")

dolomita.alimentar("Super", 35, "22/05/2026")
dolomita.alimentar("Super", 35, "26/07/2025")

dolomita.obter_historico("Alimentação")

dolomita.registrar_producao("Leite", "23/04/2026", 58)
