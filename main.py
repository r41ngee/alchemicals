import chemlib
from typing import Literal
from numpy import round
from sys import exit as sysexit

def main(action: Literal['mass_relative', 'molecular_mass', 'atomic_mass'], **kwargs) -> float | int | str:
    
    if action == 'atomic_mass':
        element_str = kwargs['element']

        element = chemlib.Element(element_str)

        if element_str == 'Cl':
            return 35.5

        else: return int(round(element.AtomicMass))
    
    elif action == 'mass_relative':
        formula = chemlib.Compound(kwargs['formula'])
        element = kwargs['element']

        return f'Доля {element} в {kwargs["formula"]}: {round(formula.percentage_by_mass(element), 2)}%'
    
    elif action == 'molecular_mass':
        formula = kwargs['formula']

        return int(round(chemlib.Compound(formula).molar_mass()))
    
def asking() -> float | int | str:
    askActionText = '''Какой режим работы?
    1. Атомная масса элемента
    2. Молекулярная масса молекулы
    3. Массовая доля элемента в молекуле
    0. Выйти
    Номер: '''

    action = input(askActionText)

    if action == '1':
        element = input('Обозначение элемента: ')

        return main('atomic_mass', element = element)
    
    elif action == '2':
        formula = input('Формула: ')

        return main('molecular_mass', formula = formula)
    
    elif action == '3':
        element = input('Обозначение элемента: ')
        formula = input('Формула: ')

        return main('mass_relative', element = element, formula = formula)
    
    elif action == '0':
        sysexit()
    
    else:
        sysexit()
    
print(asking())