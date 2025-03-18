class Person:
    def __init__(self, p_name, p_year, p_gender):
        self.name = p_name
        self.year = p_year
        self.gender = p_gender

person1 = Person("Oleg", 2024, "male")
print(person1.name)
print(person1.year)
print(person1.gender)


