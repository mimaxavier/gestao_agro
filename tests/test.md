python -m pytest -sv tests/test_animalservice.py::test_updating_weight

python -m pytest -sv tests/test_animalservice.py::test_if_object_is_ready_for_persistence

python -m pytest -sv tests/test_animalservice.py

python -m pytest -sv tests/test_animalservice.py::test_if_weight_is_less_than_1500

python -m pytest -sv tests/test_animalservice.py::test_update_animal

python -m pytest -sv tests/test_animalservice.py::test_remove_animal

python -m pytest -sv tests/test_animalservice.py::test_update_with_validate

python -m pytest -sv tests/test_animalservice.py::test_getbyid_animal

python -m pytest -sv tests/test_animal.py::test_birthdate_cannot_after_today

python -m pytest -sv tests/test_animal.py::test_calculate_age

python -m pytest -sv tests/test_animalservice.py::test_is_a_calf

# Testes MilkProductionRecord_Service
python -m pytest -sv tests/test_milkproductionrecord_service.py

python -m pytest -sv tests/test_milkproductionrecord_service.py::test_findall

python -m pytest -sv tests/test_milkproductionrecord_service.py::test_get_by_id

python -m pytest -sv tests/test_milkproductionrecord_service.py::test_update_milkproduction

python -m pytest -sv tests/test_milkproductionrecord_service.py::test_remove_milkproduction




