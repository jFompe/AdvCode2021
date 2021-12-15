from typing import List
import numpy as np
from pydash import map_


class Bingo:

  def __init__(self, table: List[List[int]]) -> None:
    self.table = np.array(table)
    self.marked = 0

  def draw_number(self, number: int) -> int:
    to_mark = self.table==number
    self.table = np.where(to_mark, -1, self.table)
    self.marked += np.sum(to_mark)
    for i in range(5):
      if np.sum(self.table[:,i]) == -5 or np.sum(self.table[i,:]) == -5:
        return self._calculate_result(number)
    return False

  def _calculate_result(self, number: int):
    return (np.sum(self.table) + self.marked) * number


class BingoManager:

  def __init__(self, draws: List[int], tables: List[Bingo]) -> None:
    self.draws = draws
    self.tables = tables

  def play_game(self) -> None:
    for d in self.draws:
      for b in self.tables:
        if (result := b.draw_number(d)) != False:
          return result

class AdvancedBingoManager(BingoManager):

    def play_to_lose(self):
      keep_checking = [True] * len(self.tables)
      for d in self.draws:
        for i,b in enumerate(self.tables):
          if not keep_checking[i]:
            continue
          if result := b.draw_number(d):
            if np.sum(keep_checking)  == 1:
              return result
            keep_checking[i] = False



def read_input(file_name: str) -> List[str]:
  tables = []
  with open(file_name, "r") as in_f:
    draws = map_(in_f.readline().strip().split(','), int)
    while in_f.readline():
      tables.append(Bingo([map_(in_f.readline().strip().split(), int) for _ in range(5)]))
  return draws, tables


def main():
  INPUT = "input.txt"
  draws, tables = read_input(INPUT)
  
  bm = BingoManager(draws, tables)
  day4_1 = bm.play_game()
  print(day4_1)

  draws, tables = read_input(INPUT)
  abm = AdvancedBingoManager(draws, tables)
  day4_2 = abm.play_to_lose()
  print(day4_2)


if __name__ == '__main__':
  main()