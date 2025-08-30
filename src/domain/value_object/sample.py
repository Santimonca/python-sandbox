from datetime import datetime

class Sample:
    def __init__(self, source_id: str, value: float):
        self.__source_id = source_id
        self.__value = value
        self.__timestamp = datetime.now()
    
    @property
    def value(self) -> float:
        return self.__value
    
    @property
    def timestamp(self) -> datetime:
        return self.__timestamp
    
    @property
    def source_id(self) -> str:
        return self.__source_id
    
    def __str__(self) -> str:
        return f"Sample(source_id={self.__source_id}, value={self.__value}, timestamp={self.__timestamp})"
    
    def __repr__(self) -> str:
        return self.__str__()
