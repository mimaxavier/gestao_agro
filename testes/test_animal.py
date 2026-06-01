from models.animal import Animal
import sys



def test_criar_animal():
    animal = Animal(1,"cow", "23/04/2024", 250)

    assert animal.codigo == 1

    assert animal.especie == "cow"

    assert animal.data_nascimento == "23/04/2024"

    assert animal.peso == 250

print(sys.path)

def test_vacinar_animal():
    animal = Animal(1,"cow", "23/04/2024", 250)

    animal.vacinar("Raiva", "26/06/2025")

    assert len(animal.historico_vacinacao) == 1

def test_obter_historico_vacinacao():
    animal = Animal(1,"cow", "23/04/2024", 250)

    animal.vacinar("Brucelose", "26/01/2026")

    vacina_name = animal.vacinar[0]

    data_vacina = animal.vacinar[1]

    historico = animal.obter_historico("Vacinação")

    assert len(historico) == 1

    assert historico[0]["Vacina"]== "Brucelose"

    assert historico[0]["Data"] == "26/01/2026"