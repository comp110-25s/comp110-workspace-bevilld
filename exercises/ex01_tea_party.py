"""COMP110 Assignment 2: Tea Party Planner"""

__author__: str = "730509911"


def main_planner(guests: int) -> None:
    """Entry point of program"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print("Cost: $" + str(cost(tea_bags(people=guests), treats(people=guests))))


def tea_bags(people: int) -> int:
    """Calculates the number of tea bags needed given guests"""
    return people * 2


def treats(people: int) -> int:
    """Calculates the number of treats needed given guests"""
    return tea_bags(people=people) * 1.5


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of the event given teas and treats needed"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
