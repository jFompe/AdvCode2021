from typing import List
import numpy as np
from pydash import map_, filter_


def read_input(file_name: str) -> List[str]:
  with open(file_name, "r") as in_f:
    return np.array([map_(list(l.strip()), int) for l in in_f.readlines()])


class Submarine:
  def __init__(self) -> None:
    self.gamma = None
    self.epsilon = None

  def power_consumption(self, values: np.ndarray) -> int:
    self.calculate_gamma_and_epsilon(values)
    return int(self.gamma,2) * int(self.epsilon,2)

  def calculate_gamma_and_epsilon(self, values: np.ndarray) -> None:
    half = len(values) // 2
    counts = np.sum(values, axis=0)
    self.gamma = ''.join(map_(counts > half, lambda x: str(int(x))))
    self.epsilon = ''.join(map_(counts < half, lambda x: str(int(x))))


class AdvancedSubmarine(Submarine):
  def __init__(self) -> None:
    super().__init__()
    self.oxygen = None
    self.co2 = None

  def life_support_rating(self, values: np.ndarray) -> int:
    self.oxygen = self.calculate_oxygen_co2(values, True)
    self.co2 = self.calculate_oxygen_co2(values, False)
    return self.oxygen * self.co2

  def calculate_oxygen_co2(self, values: np.ndarray, is_oxy: bool) -> int:
    col = 0
    while len(values) > 1:
      values = self.filter_column(values, col, is_oxy)
      col += 1
    return int(''.join(map_(values[0], str)), 2)
    
  def filter_column(self, values: np.ndarray, col: int, is_oxy: bool) -> np.ndarray:
    ones = np.sum(values[:,col])
    value = most_common(ones, len(values) - ones, is_oxy)
    return np.array(filter_(values, lambda x: x[col] == value))


def most_common(ones: int, zeros: int, inverse: bool):
  return ones >= zeros if not inverse else zeros > ones


def main():
  input = read_input("input.txt")

  s = Submarine()
  day3_1 = s.power_consumption(input)
  print(day3_1)

  s = AdvancedSubmarine()
  day3_2 = s.life_support_rating(input)
  print(day3_2)


if __name__ == "__main__":
  main()