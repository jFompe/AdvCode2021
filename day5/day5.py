from typing import List
from pydash import map_
import numpy as np


def read_input(file_name: str) -> list:
  f = lambda x: map_(x.split(","), int)
  with open(file_name, "r") as in_f:
    return [Line(*map_(r.split(" -> "),f)) for r in in_f.readlines()]


class Line:

  def __init__(self, p: list, q: list) -> None:
    self.x1, self.y1 = p
    self.x2, self.y2 = q

  def max_value(self):
    return max(self.x1, self.y1, self.x2, self.y2)


class LineManager:

  def __init__(self, lines: List[Line]) -> None:
    self.lines = lines
    self.floor = self.build_floor(lines)

  def build_floor(self, lines: List[Line]):
    high = np.max([l.max_value() for l in lines])
    floor = np.zeros((high+1,high+1))
    for l in lines:
      self.add_line(floor, l)
    return floor

  def add_line(self, floor: np.ndarray, line: Line):
    if line.x1 != line.x2 and line.y1 != line.y2:
      return
    if line.x1 == line.x2:
      for i in range(min(line.y1,line.y2), max(line.y1, line.y2)+1):
        floor[line.x1, i] += 1
    if line.y1 == line.y2:
      for i in range(min(line.x1,line.x2), max(line.x1, line.x2)+1):
        floor[i, line.y1] += 1

  def count_overlaps(self):
    return np.sum(self.floor >= 2)


class AdvancedLineManager(LineManager):

  def add_line(self, floor: np.ndarray, line: Line):
    if line.x1 == line.x2:
      self._add_vertical_line(floor, line)
    else:
      self._add_any_line(floor, line)
  
  def _add_vertical_line(self, floor: np.ndarray, line: Line):
    for i in range(min(line.y1,line.y2), max(line.y1, line.y2)+1):
      floor[line.x1, i] += 1

  def _add_any_line(self, floor: np.ndarray, line: Line):
    st_x = min(line.x1, line.x2)
    st_y = line.y1 if st_x == line.x1 else line.y2
    end_x = max(line.x1, line.x2)
    end_y = line.y1 if end_x == line.x1 else line.y2
    a = (end_y - st_y) // (end_x - st_x)
    b = st_y - a * st_x
    for i in range(st_x, end_x + 1):
      floor[i, a*i+b] += 1 


def main():
  input = read_input("input.txt")

  lm = LineManager(input)
  day5_1 = lm.count_overlaps()
  print(day5_1)

  alm = AdvancedLineManager(input)
  day5_2 = alm.count_overlaps()
  print(day5_2)


if __name__ == "__main__":  
  main()