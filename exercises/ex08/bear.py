<<<<<<< HEAD
"""File to define Bear class"""

class Bear:
    
    def __init__(self):
        return None
    
    def one_day(self):
        return None
=======
"""File to define Bear class!"""


class Bear:
    """This is the bear class!"""
    age: int
    hunger_score: int

    def __init__(self):
        """Initializes age and hunger_score."""
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        """Increments age and hunger_score."""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Updates hunger_score based on fish eaten."""
        self.hunger_score += num_fish
>>>>>>> add8592 (this is my new commits to take recursion)
