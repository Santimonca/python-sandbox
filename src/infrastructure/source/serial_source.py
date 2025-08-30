from src.domain.interfaces.source import ISource
from src.domain.value_object.sample import Sample
from serial import Serial

class SerialSource(ISource):
    def __init__(self, id: str, name: str, units: str, uart: Serial):
        super().__init__(id, name, units)

    def get_properties(self) -> dict:
        return {}
    
    def read_sample(self) -> Sample:
        pass