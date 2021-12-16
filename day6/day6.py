from pydash import map_
import numpy as np
from collections import Counter


def read_input(file: str):
  with open(file, "r") as in_f:
    return np.array(map_(in_f.readline().split(','), int))


def count_fish(fish: np.ndarray, days: int) -> int:
  return len(simulate_days(fish, days))

def simulate_days(fish: np.ndarray, days: int) -> int:
  for _ in range(days):
    count = np.count_nonzero(fish == 0)
    fish = np.where(fish == 0, 7, fish)
    fish -= 1
    fish = np.append(fish, [8] * count)
  return fish

def count_fish_efficient(fish: np.ndarray, days: int) -> int:
  return simulate_days_efficient(fish, days)


def simulate_days_efficient(fish: np.ndarray, days: int) -> int:
  counter = Counter(fish)
  for _ in range(days):
    count = counter[0]
    counter[7] += count
    for i in range(8):
      counter[i] = counter.pop(i+1, 0)
    counter[8] += count
  return sum(counter.values())
  

def main():
  input = read_input("input.txt")

  day6_1 = count_fish(input, 80)
  print(day6_1)

  day6_2 = count_fish_efficient(input, 256)
  print(day6_2)


if __name__ == "__main__":
  main()