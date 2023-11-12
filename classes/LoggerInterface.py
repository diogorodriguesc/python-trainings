from abc import abstractmethod

class LoggerInterface:
    @abstractmethod
    def info(self, message: str) -> str:
        """Log an info"""
        pass

    @abstractmethod
    def error(self, message: str) -> str:
        """Log an error"""
        pass