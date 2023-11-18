import interface
import easygui as gui

def main():
    message = 'Выберите действие:'
    screenTitle = 'Выбор действия'

    button1 = 'Атомная масса'
    button2 = 'Молекулярная масса'
    button3 = 'Массовая доля'

    result = gui.buttonbox(msg=message, title=screenTitle, choices=(button1, button2, button3))

    def writeAtomicMass() -> int | float:
        element = interface.writeElement()

        return element.atomic_mass
    
    def writeMolecularMass() -> int:
        compound = interface.writeCompound()

        return compound.getMolecularMass()
    
    def writeMassFraction():
        compound = interface.writeCompound()
        element = interface.writeElement()

        return compound.getMassFraction(element.literal, 'percentage')
    
    if result == button1:
        gui.msgbox(str(writeAtomicMass()))

    elif result == button2:
        gui.msgbox(str(writeMolecularMass()))

    elif result == button3:
        gui.msgbox(str(writeMassFraction()))

if __name__ == '__main__':
    main()