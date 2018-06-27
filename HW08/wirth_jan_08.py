"""
A few models for a game involving monsters
"""


class Monster:
  # a monster has a size and a vulnerability
  def __init__(self, size = 1, vulnerability=None):
    self.__vulnerability = vulnerability
    self.size = size
    self.number_of_victims = 0

  # number_of_victims can only be an int
  @property
  def number_of_victims(self): return self._number_of_victims

  @number_of_victims.setter
  def number_of_victims(self, value):
    try:
      self._number_of_victims = int(value)
    except ValueError:
      pass

  # a monster can grow by a certain amount of centimeters
  def grow(self, size: int) -> None:
    self.size = self.size + size

  # if the monster is big enough ( > 50cm ) it will be able to scare you
  def scare(self) -> bool:
    scary = self.size >= 50
    if scary:
      self.number_of_victims = self.number_of_victims + 1
    return scary

  # attacking the monster's vulnerable spot will shrink it by 10cm
  def attack(self, target: str) -> bool:
    hit = target == self.__vulnerability
    if hit:
      self.size = self.size - 10
    return hit

if __name__ == "__main__":
  bigMonster = Monster(size=50, vulnerability="heel")
  smallMonster = Monster(size=20, vulnerability="head")
  print("bigMonster scary? ", bigMonster.scare())
  print("smallMonster scary? ", smallMonster.scare())
  print("attack bigMonster on head", bigMonster.attack("head"))
  print("attack smallMonster on head", smallMonster.attack("head"))
  print("bigMonster still scary? ", bigMonster.scare())
  print("smallMonster still scary? ", smallMonster.scare())
  print("attack bigMonster on heel", bigMonster.attack("heel"))
  print("attack smallMonster on heel", smallMonster.attack("heel"))
  print("grow smallMonster by 10m", smallMonster.grow(1000))
  print("bigMonster still scary? ", bigMonster.scare())
  print("smallMonster still scary? ", smallMonster.scare())
  print("all ur base are belong to us")
