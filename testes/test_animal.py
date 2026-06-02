from models.animal import Animal
from models.vaccine import VaccineApplication
from datetime import datetime
from datetime import date



def test_criar_animal():
    animal = Animal(1,"cow", "23/04/2024", 250)

    assert animal.codigo == 1

    assert animal.especie == "cow"

    assert animal.data_nascimento == "23/04/2024"

    assert animal.peso == 250


def test_vacinar_animal():
    animal = Animal(1,"cow", "23/04/2024", 250)

    vacina = VaccineApplication(
        1,
        "Brucelose",
        "26/01/2026"
    )

    animal.vacinar(vacina)

    assert len(animal.historico_vacinacao) == 1

def test_obter_historico_vacinacao():
    animal = Animal(1,"cow", "23/04/2024", 250)

    vacina = VaccineApplication(
        1,
        "Brucelose",
        "26/01/2026"
    )

    animal.vacinar(vacina)

    historico = animal.obter_historico("Vacinação")

    assert len(historico) == 1

    assert historico[0].vaccine_name == "Brucelose"

    assert historico[0].apply_date == date(2026, 1, 26)

    assert historico[0].animal_id == 1

    print(type(historico[0].apply_date))

    def test_alimentar():
        animal = Animal(1, 
                  "cow",
                  "12/06/2024",
                  270
                  )
        

        alimento =