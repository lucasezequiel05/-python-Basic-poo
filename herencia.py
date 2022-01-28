class Persona:

    def __init__(self,name, last_name, age, country):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.__number = 40 #Solo se accede desde la clase. No desde la instancia
        self._color = 'blue' #Se accede desde la instancia y cualquier subclase

    def __view_info(self):
        print(f'{self.name}\n{self.last_name}\n{self.age}\n{self.country}\n')

    @property
    def get_info(self):
        return self.__view_info()

class Employer(Persona):

    def __init__(self, name, last_name, age, country):
        super().__init__(name, last_name, age, country)

class User(Persona):

    def __init__(self, name, last_name, age, country):
        super().__init__(name, last_name, age, country)

class Others(User):

    def __init__(self, name, last_name, age, country):
        super().__init__(name, last_name, age, country)
    
if __name__ == '__main__':

    david = Employer('david', 'ottamendi', 33, 'Argentina')
    jessica = User('jessica','cardinal',25,'Uruguay')

    #jessica.__view_info()  No accede al metodo privado.
    david.get_info

    sech = Persona('sech', 'armstrong', 40, 'USA')
    sech.get_info
    
    
    #print(david._color+'\n') #Accede al atributo protegido.
    #print(david.__number) No accede al atributo privado.

    regina = Others('regina', 'cambridge', 30, 'New Zeland')
    regina.get_info

    print(regina._color)
