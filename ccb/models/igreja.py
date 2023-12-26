from typing import Dict


class Igreja:
    def __init__(self, _id: str, cod: str, igreja: str, cultos: Dict[str, str]):
        self._id = _id
        self.cod = cod
        self.igreja = igreja
        self.cultos = cultos

    def to_dict(self):
        return {
            '_id': self._id,
            'cod': self.cod,
            'igreja': self.igreja,
            'cultos': self.cultos
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data['_id'],
            cod=data['cod'],
            igreja=data['igreja'],
            cultos=data['cultos']
        )
