"""Instantiate a River and Run The Simulation!"""

from exercises.ex08.river import River

my_river: River = River(10, 2)
print(my_river.bears)
my_river.one_river_week()
print(my_river.bears)

    
