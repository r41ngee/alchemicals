import json
from typing import Literal

ELEMENTS_FILENAME = 'elements.json'
with open(ELEMENTS_FILENAME, 'r') as file:
    _elements_list = json.load(file)



class Element:
    def __init__(
            self, 
            literal: str,
            atomic_number: int,
            atomic_mass: int | float,
            period: int,
            group: int,
            subgroup: Literal['A', 'B']
        ) -> None:
        
        self.literal = literal
        self.atomic_number = atomic_number
        self.atomic_mass = atomic_mass
        self.period = period
        self.group = group
        self.subgroup = subgroup

    def getElement(self, literal: str):
        element = _elements_list[literal]

        return Element(
            literal,
            element['atomic_number'],
            element['atomic_mass'],
            element['period'],
            element['group'],
            element['subgroup']
        )