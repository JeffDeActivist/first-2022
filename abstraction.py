"""keeps record of names of all workers,
calculates the commision each should get then the total earning for each worker"""


# Angayo Jeff     TU01-SC211-1174/2020


class Employers:
    names = []  # names and salaries of all employers will be added to this list

    def __init__(self, name, age, salary, role):
        self.name = name
        self.age = age
        """encapsulation"""
        self.__salary = salary  # cannot be accessed directly outside the class methods......encapsulation
        self.role = role
        Employers.names.append(self.get_totals())  # appends result of get_totals
        """abstraction"""

    def __commission(self):  # a level of abstraction this method cannot be accessed outside this class.Can  attempt
        if self.role == 'manager':
            return self.__salary * 0.5
        elif self.role == 'CEO':
            return self.__salary * 0.4
        else:
            return self.__salary * 0.2

    def get_totals(self):  # using the level of abstraction above to determine total earns
        return self.name, self.__commission() + self.__salary


w1 = [Employers("jeff", 15, 300000, "manager"),  # user can input salary btw
      Employers("angayo", 21, 3000, "CEO"),
      Employers("Mwai", 24, 29200, "Chief"),
      Employers("tecno", 23, 8000, " supervisor")]

# print(w1[0].name, w1[0].age, w1[0].role, w1[0].__salary)  # cannot print salary in the w1 list
print(w1[1].get_totals())

"""inheritance"""


# we are overriding class Employers by creating new objects in class SeniorWorkers


class Manager(Employers):
    def __init__(self, name, age, salary, role, senior_role):
        super().__init__(name, age, salary, role)
        self.senior_role = senior_role

    def get_name_senior_role(self):
        return f"{self.name} is the {self.senior_role} of this company"


m1 = Manager("jeff", 18, 80000, "CEO", "Editor")
print(m1.get_name_senior_role())
print(m1.get_totals())
print(m1.name, m1.senior_role, m1.role)
print(Employers.names)

# I have appended this from another module
