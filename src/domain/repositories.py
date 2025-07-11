from abc import ABC, abstractmethod

class UserRepositoryInterface(ABC):
    @abstractmethod
    def create(self, user: dict):
        pass

    @abstractmethod
    def find_by_email(self, email: str):
        pass

    
    @abstractmethod
    def find_by_id(self, user_id: str) -> dict | None:
        pass

    @abstractmethod
    def find_all(self) -> list[dict]:
        """Retorna todos los usuarios registrados."""
        pass
