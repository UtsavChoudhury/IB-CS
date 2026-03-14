class Newspaper():
    def __init__(self, name, year, month, day_of_month, is_finnish):
        self.__name = name
        self.year = year
        self.month = month
        self.day_of_month = day_of_month
        self.is_finnish = is_finnish

    def get_name(self):
        return self.__name

    def __str__(self):
        return (f'NEWSPAPER DETAILS: [NAME = {self.get_name()}], ' 
                f'[YEAR = {self.year}], [MONTH = {self.month}], '
                f'[DAY = {self.day_of_month}], [IS FINNISH = {self.is_finnish}]')                # Create an object of the Newspaper class


newspaper = Newspaper("Helsingin Sanomat", 2023, 10, 5, True)
                
print(newspaper)
                

print("Newspaper Name:", newspaper.get_name())