from models.animal import Animal
from repositories.animal_repository import AnimalRepository
from datetime import datetime

class AnimalService:

    def __init__(self, repository = None):
        self.repository = repository or AnimalRepository()

    def register(self, animal):
        self.repository.save(animal)

    def update(self, animal):
        self.repository.update(animal)

    def remove(self, id):
        self.repository.delete(id)

    def get_by_id(self, id):
        return self.repository.get_by_id(id)


