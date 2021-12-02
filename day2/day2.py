from typing import List


def read_input(file_name: str) -> List[str]:
  with open(file_name, "r") as in_f:
    lines = [l.strip().split(" ") for l in in_f.readlines()]
  return [(move, int(am)) for move, am in lines]


class Submarine:
  def __init__(self) -> None:
    self.horizontal = 0
    self.depth = 0

  def move(self, dir, amount) -> None:
    if dir == 'forward':
      self.horizontal += amount
    if dir == 'up':
      self.depth -= amount
    if dir == 'down':
      self.depth += amount

  def result(self) -> int:
    return self.horizontal * self.depth

class AdvancedSubmarine(Submarine):
  def __init__(self) -> None:
    super().__init__()
    self.aim = 0

  def move(self, dir, amount) -> None:
    if dir == 'forward':
      self.horizontal += amount
      self.depth += self.aim * amount
    if dir == 'up':
      self.aim -= amount
    if dir == 'down':
      self.aim += amount

def calculate_result(sub, moves):
  for m in moves:
    sub.move(*m)
  return sub.result()


def main():
  input = read_input("input.txt")
  print(input)

  day2_1 = calculate_result(Submarine(), input)
  print(day2_1)

  day2_2 = calculate_result(AdvancedSubmarine(), input)
  print(day2_2)


if __name__ == "__main__":
  main()