import easygui as gui
import elemental

def writeCompound() -> elemental.Compound:
    windowTitle = 'Ввод формулы'
    message = 'Введите формулу'

    inputField = gui.enterbox(msg=message, title=windowTitle)
    return elemental.Compound.getCompound(inputField)

def writeElement() -> elemental.Element:
    windowTitle = 'Ввод элемента'
    message = 'Введите элемент:'

    inputField = gui.enterbox(msg=message, title=windowTitle)
    return elemental.Element.getElement(inputField)