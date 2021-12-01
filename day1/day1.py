from typing import List


def read_input(file_name: str) -> List[str]:
  with open(file_name, "r") as in_f:
    return list(map(int, in_f.readlines()))


def count_increases(depths: List[int]) -> int:
  return sum([depths[i] > depths[i-1] for i in range(1,len(depths))])

def count_every_three_increases(depths: List[int]) -> int:
  return sum([depths[i] > depths[i-3] for i in range(3,len(depths))])


def main():
  input = read_input("input.txt")
  
  day1_1 = count_increases(input)
  print(day1_1)

  day1_2 = count_every_three_increases(input)
  print(day1_2)


if __name__ == "__main__":
  main()