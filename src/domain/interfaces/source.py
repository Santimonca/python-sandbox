from abc import ABC, abstractmethod
from src.domain.value_object.sample import Sample

class ISource(ABC):
    def __init__(self, id: str, name: str, units: str):
        self.__id = id
        self.__name = name
        self.__units = units

    def get_id(self) -> str:
        return self.__id

    def get_name(self) -> str:
        return self.__name
    
    def get_units(self) -> str:
        return self.__units
    
    @abstractmethod
    def get_properties(self) -> dict:
        pass

    @abstractmethod
    def read_sample(self) -> Sample:
        pass
