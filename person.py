from typing import List

class Person:

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_info(self):
        return ({'name':self.name,'age':self.age})

list_person: List[Person] = []

def addPerson(name: str, age: int):

    aPerson = Person(name= name, age= age)
    list_person.append(aPerson)

def getPeople():

    respond = [person.get_info() for person in list_person]

    return respond