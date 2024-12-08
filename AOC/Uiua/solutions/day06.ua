# Experimental!
Input ← (
  &fras "./data/day06.txt"
  ▽≠,@\r  # remove carriage return
  ⊜∘≠,@\n # split on newlines
)
W        ← ⧻⊢Input    # width
H        ← ⧻Input     # height
SP       ← ⊢⊚⌕@^Input # start position
SD       ← [¯1 0]     # start direction 
R        ← ⍜⊣¯⇌       # rotate direction
N ← (
  ⍜⊙↘₁(⊂⟜+⍥R⊙(⊃↙↘2)) # next coord by rotating x times
  ⍜⊢+₁               # increment the counter 
)
Valid    ← /↧[⊃⊓(<W|<H)∩≥₀°⊟] # valid coordinate
Check    ← ≠@#⍣⊡@.⊙Input≡↘3   # check neighbours not #
Neis ← (
  [⊃(N0|N1|N2|N3)] # neighbours
  ▽⊸Check          # keep unobstructed positions
)
FindPath ← (
  ⊂SD SP # start pos and direction
  ⊂0     # counter (to avoid astar omitting loops)
  °□⊢ astar(
    °⊏ Neis  # neighbours with no rotation = lowest cost
  | 0        # heuristic of 0
  | ¬Valid↘3 # keep going until out of grid
  )
  ⊙◌  # discard the cost
  ↘¯1 # the last one is out of the grid
)

# Part A
⧻◴≡↘₃FindPath # how many unique path positions
