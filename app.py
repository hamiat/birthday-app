from datetime import date, timedelta


class Person:
    def __init__(self, name: str, age_delta: timedelta):
        self.name = name
        self.age_delta = age_delta


def validate_date(date_string) -> bool:
    try:
        date.fromisoformat(date_string)
        return True
    except ValueError:
        return False


def add_people(separator: str, people: list):
    while True:
        name = input("Please enter a name: ")

        if not name.strip():
            print("❌  Name cannot be empty.\n")
            continue

        if name.lower() == "x":
            print(f"Goodbye! Processing data...\n")
            break

        birthday = input("Please enter birthday (yyyy-mm-dd): ").strip()

        if validate_date(birthday):
            birthday = date.fromisoformat(birthday)
            today = date.today()
            person = Person(name, today - birthday)
            people.append(person)
            print(f"✔️   {person.name} was added! \n\n{separator}")
        else:
            print(
                f"❌  {name} was not added due to incorrect birthday format (should be yyyy-mm-dd).\n\n{separator}"
            )


def display_result(people: list[Person]):
    divider = "=" * 10

    print(f"{divider} Result {divider}")

    if len(people) > 1:
        people_sorted = sorted(
            people, key=lambda person: person.age_delta, reverse=True
        )
        oldest = people_sorted[0]
        youngest = people_sorted[-1]
        print(f"The oldest is {oldest.name} and youngest is {youngest.name}.")
    elif len(people) == 1:
        print(
            f"Only one person ({people[0].name}) was added, so they are the oldest and youngest."
        )
    else:
        print("No data was found.")

    print(f"{divider * 2}========")


def main():
    people = []
    separator = "-" * 36

    print(
        "\n=== Welcome to my app! ===\n"
        "Add a name and a birthday for as many people as you want.\n"
        "When you are done, type 'x' to finish. I'll tell you who is the oldest and who is the youngest.\n\n"
        f"{separator}"
    )

    add_people(separator, people)
    display_result(people)


if __name__ == "__main__":
    main()
