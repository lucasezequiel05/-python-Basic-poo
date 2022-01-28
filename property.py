import string


class Personaje:

    def __init__(self, name):
        self.name = name
        self.__element = self.__assignElement()
    
    def __assignElement(self):
        return 'water'

    @property
    def element(self):
        return self.__element

    @element.setter
    def setElement(self, newElement):
        if isinstance(newElement, str):
            self.__element = newElement
        else:
            print('You must assign a String')
    
    @element.deleter
    def deleteElement(self):
        del self.__element
        print('The element has been deleted')

if __name__ == '__main__':

    camus = Personaje('camus')
    print(camus.name)
    print(camus.element)

    camus.setElement = 'fire'
    print(camus.element)

    del camus.deleteElement
    print(camus.element) # It throws an error when not finding attribute.
