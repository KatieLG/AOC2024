Expected ← (
  [{2000468 18567089}                   # day 1
   {242 311}                            # day 2
   {181345830 98729041}                 # day 3
   {2575 2041}                          # day 4
   {4662 5900}                          # day 5
   {4374 1705}                          # day 6
   {2664460013123 426214131924213}      # day 7
   {222 884}                            # day 8
   {6378826667552 6413328569890}        # day 9
   {430 928}                            # day 10
   {212655 253582809724830}             # day 11
   {1473408 886364}                     # day 12
   {31589 98080815200063}               # day 13
   {222208000 7623}                     # day 14
   {1406628 1432781}                    # day 15
   {85420 492}                          # day 16
   {"1,5,0,1,7,4,1,0,3" 47910079998866} # day 17
   {322 "60,21"}                        # day 18
   {226 601201576113503}                # day 19
   {1363 1007186}                       # day 20
   {278748 ∞}                           # day 21
   {14726157693 1614}                   # day 22
   {3065 "None"}                        # day 25
  ]
)
SolutionMap ← map+1⇡⊸⧻Expected
GetSolution ← get⊙SolutionMap

TestDay ← (
  ⟜(&p $"Executing tests for day _" ↙₋₂$"0_")
  ⊙:
  GetSolution                                   # get the actual solution
  ⊙:∩°□⊃⊢⊣                                      # align with outputs
  ⍤.≍                                           # assert part a is correct
  ⍤.≍                                           # assert part b is correct
  &p $"Tests passed with runtime: _s\n" ⁅₃¯-now # output runtime
)

NoSolution ← "No Solution"
TooLong    ← "Runtime too long"
Missingb   ← "Missing part b"
SkipDay ← (
  &p $"Skipping tests for day _: _\n" ↙₋₂$"0_" # skip with reason
)

# ---- Tests -----
now
~ "../solutions/day01.ua"
TestDay 1

now
~ "../solutions/day02.ua"
TestDay 2

now
~ "../solutions/day03.ua"
TestDay 3

now
~ "../solutions/day04.ua"
TestDay 4

now
~ "../solutions/day05.ua"
TestDay 5

# TODO
SkipDay 6 TooLong

now
~ "../solutions/day07.ua"
TestDay 7

now
~ "../solutions/day08.ua"
TestDay 8

# TODO
SkipDay 9 Missingb

now
~ "../solutions/day10.ua"
TestDay 10

now
~ "../solutions/day11.ua"
TestDay 11

now
~ "../solutions/day12.ua"
TestDay 12

now
~ "../solutions/day13.ua"
TestDay 13

now
~ "../solutions/day14.ua"
TestDay 14

# TODO
SkipDay 15 NoSolution

now
~ "../solutions/day16.ua"
TestDay 16

now
~ "../solutions/day17.ua"
TestDay 17

now
~ "../solutions/day18.ua"
TestDay 18

now
~ "../solutions/day19.ua"
TestDay 19

SkipDay 20 TooLong

SkipDay 21 NoSolution

SkipDay 22 TooLong

SkipDay 23 NoSolution

SkipDay 24 NoSolution

now
~ "../solutions/day25.ua"
"None" # no part b for day 25
TestDay 25
