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
SkipDay 6 "runtime is too long"

now
~ "../solutions/day07.ua"
TestDay 7

now
~ "../solutions/day08.ua"
TestDay 8

# TODO
SkipDay 9 "Missing part b"

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
SkipDay 15 "Not done yet"

now
~ "../solutions/day16.ua"
TestDay 16

now
~ "../solutions/day17.ua"
TestDay 17
