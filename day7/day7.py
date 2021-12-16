from pydash import map_
import numpy as np


def read_input(file: str):
  with open(file, "r") as in_f:
    return np.array(map_(in_f.readline().split(','), int))


def calculate_distances(points):
  return np.min([np.sum(np.abs(i-points)) for i in range(np.max(points))])


def triangular_number(n):
    return n * (n + 1) // 2

def calculate_unconstant_distances(points):
  return np.min([np.sum(triangular_number(np.abs(i-points))) for i in range(np.max(points))])


def main():
  input = read_input("input.txt")

  day7_1 = calculate_distances(input)
  print(day7_1)

  day7_2 = calculate_unconstant_distances(input)
  print(day7_2)


if __name__ == "__main__":
  main()