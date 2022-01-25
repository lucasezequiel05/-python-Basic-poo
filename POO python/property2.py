countries = ['mexico','usa','canada','brasil']

class Persona:

    def __init__(self, name):
        self.__name = name.lower()
        self.__country = None
    
    #create a getter for __country property:
    @property
    def country(self):

        if self.__country == None:
            print('No value assigned yet')
        else:
            print(f'{self.__country}')
    
    #Setter to country property.
    #Don't need have the same name but, must call the method with setCountry
    @country.setter
    def set_country(self, new_country):

        if new_country.lower() in countries:
            self.__country = new_country
        else:
            print(f'The value {new_country} is not allowed.\nPlease enter {countries}.')

    @property
    def get_email(self):
        print (f'{self.__name.lower()}.{self.__country.lower()}@gmail.com')
    
if __name__ == '__main__':

    employer = Persona('DAnte')
    employer.set_country = 'brasiL'
    employer.country
    employer.get_email
    