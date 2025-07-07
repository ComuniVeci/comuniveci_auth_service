from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    def create(self, user: dict):
        pass

    @abstractmethod
    def find_by_email(self, email: str):
        pass
