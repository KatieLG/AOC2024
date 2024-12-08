# Experimental!
Input ← (
  &fras "./data/day06.txt"
  ▽≠,@\r  # remove carriage return
  ⊜∘≠,@\n # split on newlines
)
W ← ⧻⊢Input            # width
H ← ⧻Input             # height
R ← ⍜⊣¯⇌               # rotate direction
N ← ⍜⊙↘₁(⊂⟜+⍥R⊙(⊃↙↘2)) # next coord by rotating x times

Valid ← /↧[⊃⊓(<W|<H)∩≥₀°⊟] # valid coordinate
Check ← ≠@#⍣⊡@.≡↘3         # check neighbours not #
Neis ← (
  [⊃(N0|N1|N2|N3)] # neighbours
  ≡⍜⊢+₁            # increment counter
  ▽⤚Check          # keep unobstructed positions
)
FindPath ← (
  .
  ⊂[¯1 0]⊢⊚⌕@^ # start pos and direction
  ⊂0           # counter (to avoid astar omitting loops)
  °□⊢ astar(
    °⊏ Neis  # neighbours with no rotation = lowest cost
  | 0        # heuristic of 0
  | ¬Valid↘3 # keep going until out of grid
  )
  ⊙◌  # discard the cost
  ↘¯1 # the last one is out of the grid
)

# Part A
◴≡↘₃FindPath Input # unique path positions
⧻                  # count 
