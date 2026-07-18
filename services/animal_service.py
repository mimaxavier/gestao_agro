from models.animal import Animal
from repositories.animal_repository import AnimalRepository
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class AnimalService:

    def __init__(self, repository = None):
        self.repository = repository or AnimalRepository()

    def register(self, animal):
        self.repository.save(animal)

        logger.info(f"Registrando animal de ID = {animal.id}.")

    def findall(self):
        self.repository.find_all()

        logger.info(f"Buscando todos os registros de animal.")

    def update(self, animal):
        self.repository.update(animal)

        logger.info(f"Atualizando animal de ID = {animal.id}")

    def remove(self, id):
        self.repository.delete(id)

        logger.info(f"Animal ID = {id} removido!")

    def get_by_id(self, id):
        return self.repository.get_by_id(id)
    


