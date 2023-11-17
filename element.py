import json
from typing import Literal
from numpy import round

ELEMENTS_FILENAME = 'elements.json'
with open(ELEMENTS_FILENAME, 'r') as file:
    _elements_list = json.load(file)



class Element:
    '''
    Класс элемента.
    Экземпляр можно получить методом класса ``getElement()``.
    '''

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

    def getElement(literal: str) -> "Element":
        '''
        Возвращает объект класса ``Element``.
        Принимает латинские символы элемента как аргумент.
        '''
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
    '''
    Класс химического соединения. Метод получения ещё не дописан.
    '''
    def __init__(self, elements: tuple[dict[Element, int | float]]) -> None:
        self.elements = elements

    def getMolarMass(self):
        mass = 0

        for i in self.elements:
            mass += int(round(i['element'].atomic_mass)) * int(i['index'])

        return mass
    
    def getCompound() -> "Compound":
        '''
        Не готово.
        '''
        ...