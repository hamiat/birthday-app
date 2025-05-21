import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def validate_date(date_string):
    try:
        datetime.date.fromisoformat(date_string)
        return True
    except ValueError:
        return False
    
people = []
stars = '*' * 12

print(f"***Hello, welcome to my app!***\nAdd a name and a birthday for as many people as you want.\nWhen you are done, type 'x' to exit and the app will tell you who is the oldest and who is the youngest.")

while True:
    name = input("Please enter a name: ")

    if name == "x" or name == "X":
        print("Bye for now!")
        break
    else:
        today = datetime.date.today()
        birthday = input("Please enter birthday (yyyy-mm-dd): ")

        if validate_date(birthday):
            birthday = datetime.date.fromisoformat(birthday)
            age = birthday
            person = Person(name, today - birthday)
            people.append(person)
            print(f"{person.name} was added! \n{stars}")
        else:
            print(f"Incorrect date, should be yyyy-mm-dd. {name} was not added. \n{stars}")

if len(people) > 0:
    people_sorted = sorted(people, key=lambda person: person.age)
    youngest = people_sorted[0]
    oldest= people_sorted[-1]
    print(f"{stars}\nResult: \nThe oldest is {oldest.name} and youngest is {youngest.name}\n{stars}")

