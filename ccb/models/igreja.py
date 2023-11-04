from typing import Dict


class Igreja:
    def __init__(self, _id: str, cod: str, igreja: str, horarios: Dict[str, str]):
        self._id = _id
        self.cod = cod
        self.igreja = igreja
        self.horarios = horarios

    def to_dict(self):
        return {
            '_id': self._id,
            'cod': self.cod,
            'igreja': self.igreja,
            'horarios': self.horarios
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            _id=data['_id'],
            cod=data['cod'],
            igreja=data['igreja'],
            horarios=data['horarios']
        )
