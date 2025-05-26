import datetime

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def validate_date(date_string) -> bool:
    try:
        datetime.date.fromisoformat(date_string)
        return True
    except ValueError:
        return False
    
people = []
equals_signs = "=" * 10
dashes = "-" * 36  

print(f"\n=== Welcome to my app!===\nAdd a name and a birthday for as many people as you want.\nWhen you are done, type 'x' to finish. I'll tell you who is the oldest and who is the youngest.\n\n{dashes}")

def add_people():
    while True:
        name = input("Please enter a name: ")

        if name == "x" or name == "X":
            print(f"Goodbye! Processing data...\n")
            break
        else:
            today = datetime.date.today()
            birthday = input("Please enter birthday (yyyy-mm-dd): ")

            if validate_date(birthday):
                birthday = datetime.date.fromisoformat(birthday)
                person = Person(name, today - birthday)
                people.append(person)
                print(f"✔️   {person.name} was added! \n\n{dashes}")
            else:
                print(f"❌  {name} was not added due to incorrect birthday format, should be yyyy-mm-dd.  \n\n{dashes}")

add_people()
print(f"{equals_signs} Result {equals_signs}")

if len(people) > 1:
    people_sorted = sorted(people, key=lambda person: person.age)
    youngest = people_sorted[0]
    oldest= people_sorted[-1]
    print(f"The oldest is {oldest.name} and youngest is {youngest.name}")
elif len(people) == 1:
    print(f"Only one person ({people[0].name}) was added, so they are the oldest and youngest.")
else:    
    print("No data was found.")

print(f"{equals_signs * 2}========")



