import json
from typing import Literal
from numpy import round
from chemlib.parse import parse_formula

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
    Класс химического соединения. Метод получения по формуле - ``getCompound``.
    '''
    def __init__(self, elements: dict[str: int]) -> None:
        def __transform_to_elements__(elems: dict) -> list:
            elem_list = list(elems.keys())
            index_list = list(elems.values())
            out = []

            assert len(elem_list) == len(index_list)

            for i in range(len(elem_list)):
                out.append([elem_list[i], index_list[i]])

            return out
        
        self.elementsDicted = elements
        self.elementsTupled: list[Element, int] = __transform_to_elements__(elements)

    def getMolecularMass(self) -> int:
        mass = 0
        for i in self.elementsTupled:
            mass += Element.getElement(i[0]).atomic_mass * i[1]

        return mass
    
    def getCompound(formula: str) -> "Compound":
        '''
        Возвращает объект ``Compound`` по формуле.
        '''
        return Compound(parse_formula(formula))
    
    def getMassFraction(self, element_lit: str, return_type: Literal['percentage', 'float'] = 'float'):
        '''
        Возвращает массовую долю элемента в соединении
        '''
        if return_type == 'percentage':
            return f'{float(round((Element.getElement(element_lit).atomic_mass * self.elementsDicted[element_lit]) / self.getMolecularMass(), 4)) * 100}%'
        
        elif return_type == 'float':
            return float(round((Element.getElement(element_lit).atomic_mass * self.elementsDicted[element_lit]) / self.getMolecularMass(), 4))
        
        else:
            raise Exception(f'Incorrect return type: {return_type}')