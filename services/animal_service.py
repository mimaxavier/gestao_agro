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

        
        if animal.weight>1500:
            raise ValueError("O animal não pode ter peso superior a 1500kg")
        

    def _validate_if_animal_exists(self, id):
        animal_db = self.get_by_id(id)

        if animal_db is None:
            raise ValueError("O registro não existe!")
        else:
            return id

    def _validate_weight(self, animal):
        if animal.weight>1500:
            raise ValueError("O animal não pode ter mais de 1500kg")

        
    # CRUD methods

    def register(self, animal):
        self._validate_object_is_ready_for_register(animal)
        self._validate_weight(animal)
        self.repository.save(animal)

        logger.info(f"Registrando animal de ID = {animal.id}.")

    def findall(self):
        logger.info(f"Buscando todos os registros de animal.")

        return self.repository.find_all()

    def update(self, animal):
        self._validate_if_animal_exists(animal.id)
        self._validate_weight(animal)
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

    # Business Rules

    

    '''def calf_not_production(self, animal):
        if self.is_a_calf(animal):
            raise ValueError("Este animal não está pronto pra produzir")'''


        






    
    
    