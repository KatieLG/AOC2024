Expected ← (
  [[2000468 18567089]              # day 1
   [242 311]                       # day 2
   [181345830 98729041]            # day 3
   [2575 2041]                     # day 4
   [4662 5900]                     # day 5
   [4374 1705]                     # day 6
   [2664460013123 426214131924213] # day 7
   [222 884]                       # day 8
   [6378826667552 6413328569890]   # day 9
   [430 928]                       # day 10
   [212655 253582809724830]        # day 11
   [1473408 886364]                # day 12
   [31589 98080815200063]          # day 13
   [222208000 7623]                # day 14
   [1406628 1432781]               # day 15
  ]
)
SolutionMap ← map+1⇡15 Expected
GetSolution ← get⊙SolutionMap

TestDay ← (
  ⟜(&p $"Executing tests for day _" ↙₋₂$"0_")
  GetSolution⊙(⇌⊟) # get the actual solution
  ⍤.≍              # assert matching
)

# ---- Tests -----
~ "../solutions/day01.ua"
TestDay 1

~ "../solutions/day02.ua"
TestDay 2

~ "../solutions/day03.ua"
TestDay 3

~ "../solutions/day04.ua"
TestDay 4

~ "../solutions/day05.ua"
TestDay 5

# TODO - improve runtime
# ~ "../solutions/day06.ua"
# TestDay 6

~ "../solutions/day07.ua"
TestDay 7

~ "../solutions/day08.ua"
TestDay 8

# TODO - part b
# ~ "../solutions/day09.ua"
# TestDay 9

~ "../solutions/day10.ua"
TestDay 10

# TODO - check why recursion limit is being exceeded
# ~ "../solutions/day11.ua"
# TestDay 11

# TODO
# ~ "../solutions/day12.ua"
# TestDay 12

~ "../solutions/day13.ua"
TestDay 13

~ "../solutions/day14.ua"
TestDay 14

# TODO
# ~ "../solutions/day15.ua"
# TestDay 15
