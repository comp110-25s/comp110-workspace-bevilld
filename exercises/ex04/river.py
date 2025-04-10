"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        bears: list[Bear] = self.bears
        fish: list[Fish] = self.fish
        for i in fish:
            if i.age <= 3:
                fish.append(i)
        for i in bears:
            if i.age <= 5:
                bears.append(i)
        self.bears = bears
        self.fish = fish
        return None

    def remove_fish(self, amount: int):
        idx: int = 0
        while idx < amount:
            self.fish.pop(0)
            idx += 1
        return None

    def bears_eating(self):
        for i in self.bears:
            if len(self.fish) > 5:
                self.remove_fish(3)
                i.eat(3)
        return None

    def check_hunger(self):
        bears: list[Bear] = []
        for i in self.bears:
            if i.hunger_score >= 0:
                bears.append(i)
        self.bears = bears
        return None

    def repopulate_fish(self):
        idx: int = 0
        spawn: int = (len(self.fish) // 2) * 4
        while idx < spawn:
            self.fish.append(Fish())
            idx += 1
        return None

    def repopulate_bears(self):
        idx: int = 0
        cubs: int = len(self.bears) // 2
        while idx < cubs:
            self.bears.append(Bear())
            idx += 1
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        idx = 0
        while idx < 7:
            self.one_river_day()
            idx += 1
        return None
