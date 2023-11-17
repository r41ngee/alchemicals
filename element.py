import json
from typing import Literal
from numpy import round

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

    def getElement(literal: str):
        element = _elements_list[literal]

        return Element(
            literal,
            element['atomic_number'],
            element['atomic_mass'],
            element['period'],
            element['group'],
            element['subgroup']
        )
    
class Compound:
    def __init__(self, elements: tuple[dict[Element, int | float]]) -> None:
        self.elements = elements

    def getMolarMass(self):
        mass = 0

        for i in self.elements:
            mass += int(round(i['element'].atomic_mass)) * int(i['index'])

        return mass
    
print(Compound([
    {
        'element': Element.getElement('H'),
        'index': '2'
    },
    {
        'element': Element.getElement('O'),
        'index': 1
    }
]).getMolarMass())