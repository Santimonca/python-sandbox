from collections import deque
from src.domain.value_object.sample import Sample

class Signal:
    def __init__(self, length: int = 10):
        self.__buffer = deque(maxlen=length)
        self.__last_sample_source_id = None
    
    def add_sample(self, sample: Sample):
        if self.__last_sample_source_id is None:
            pass
        else:
            if self.__last_sample_source_id != sample.source_id:
                raise ValueError("Sample source ID does not match signal source ID")
        
        self.__last_sample_source_id = sample.source_id
        self.__buffer.append(sample)
    
    def get_samples(self) -> list[Sample]:
        return list(self.__buffer)
    
    def get_last_sample(self) -> Sample:
        return self.__buffer[-1]