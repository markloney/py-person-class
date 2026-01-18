class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people_list: list) -> list:
    persons = []

    for people_item in people_list:
        persons.append(Person(people_item["name"], people_item["age"]))

    for people_item in people_list:

        if "wife" in people_item and people_item["wife"] is not None:
            Person.people[people_item["name"]].wife \
                = Person.people[people_item["wife"]]

        elif "husband" in people_item and people_item["husband"] is not None:
            Person.people[people_item["name"]].husband \
                = Person.people[people_item["husband"]]

    return persons
