<<<<<<< HEAD
"""File to define River class"""
=======
"""File to define River class!"""
>>>>>>> add8592 (this is my new commits to take recursion)

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear

<<<<<<< HEAD
class River:
    
    def __init__(self, num_fish: int, num_bears:int):
        """New River with num_fish Fish and num_bears Bears"""
=======

__author__ = "730664874"


class River:
    """This is the river class!"""
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears!"""
>>>>>>> add8592 (this is my new commits to take recursion)
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())
<<<<<<< HEAD

    def check_ages(self):
        return None

    def bears_eating(self):
        return None
    
    def check_hunger(self):
        return None
        
    def repopulate_fish(self):
        return None
    
    def repopulate_bears(self):
        return None
    
    def view_river(self):
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river"""
=======
    
    def remove_fish(self, amount: int):
        """Removes inputted amount of fish from fish list."""
        new_fish: list[Fish] = list()
        for index in range(amount, len(self.fish)):
            new_fish.append(self.fish[index])
        self.fish = new_fish
    
    def bears_eating(self):
        """Updated bears' hunger scores based on fish."""
        for bear in self.bears:
            if (len(self.fish) > 5):
                self.remove_fish(3)
                bear.eat(3)
    
    def check_hunger(self):
        """Removes bear if hunger_score < 0."""
        new_bears: list[Bear] = list()
        for bear in self.bears:
            if (bear.hunger_score >= 0):
                new_bears.append(bear)
        self.bears = new_bears
                
    def check_ages(self):
        """Removes fish and bears based on age."""
        new_fish: list[Fish] = list()
        new_bears: list[Fish] = list()
        for fish in self.fish:
            if (fish.age <= 3):
                new_fish.append(fish)
        self.fish = new_fish
        for bear in self.bears:
            if (bear.age <= 5):
                new_bears.append(bear)
        self.bears = new_bears
        
    def repopulate_fish(self):
        """Adds new fish to fist list."""
        for index in range((len(self.fish) // 2) * 4):
            self.fish.append(Fish())
    
    def repopulate_bears(self):
        """Adds new bears to bear list."""
        for index in range(len(self.bears) // 2):
            self.bears.append(Bear())
            
    def view_river(self):
        """Displays properties of the river."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
            
    def one_river_day(self):
        """Updates data for the river for one day."""
>>>>>>> add8592 (this is my new commits to take recursion)
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
<<<<<<< HEAD
=======

    def one_river_week(self):
        """Updates river by 7 days."""
        for index in range(7):
            self.one_river_day()
>>>>>>> add8592 (this is my new commits to take recursion)
            
