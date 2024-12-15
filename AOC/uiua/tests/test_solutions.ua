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
