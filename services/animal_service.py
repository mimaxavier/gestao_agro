from models.animal import Animal
from repositories.animal_repository import AnimalRepository
from datetime import datetime, date
import logging

logger = logging.getLogger(__name__)

class AnimalService:

    def __init__(self, repository = None):
        self.repository = repository or AnimalRepository()

    # Validates Methods

    def _validate_object_is_ready_for_register(self, animal):

        if animal.id is not None:
            raise ValueError("O registro já existe.")
        

    def _validate_if_animal_exists(self, animal):
        animal_db = self.get_by_id(animal.id)

        if animal_db is None:
            raise ValueError("O registro não existe!")
        else:
            return animal
        
    # CRUD methods

    def register(self, animal):
        self._validate_object_is_ready_for_register(animal)
        self.repository.save(animal)

        logger.info(f"Registrando animal de ID = {animal.id}.")

    def findall(self):
        logger.info(f"Buscando todos os registros de animal.")

        return self.repository.find_all()

    def update(self, animal):
        self._validate_if_animal_exists(animal)
        self.repository.update(animal)

        logger.info(f"Atualizando animal de ID = {animal.id}")

    def remove(self, id):
        self._validate_if_animal_exists(id)
        self.repository.delete(id)

        logger.info(f"Animal ID = {id} removido!")

    def get_by_id(self, id):
        return self.repository.get_by_id(id)
    
    
    # Update Weight
    
    def update_weight(self, animal, current_weight):
        
        animal.weight = current_weight

        return self.update(animal)






    
    
    