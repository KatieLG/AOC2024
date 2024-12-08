# Experimental!
Input ← (
  &fras "./data/day06.txt"
  ▽≠,@\r  # remove carriage return
  ⊜∘≠,@\n # split on newlines
)

W     ← ⧻⊢Input            # width
H     ← ⧻Input             # height
R     ← ⍜⊣¯⇌               # rotate direction
N     ← ⊂⟜+⍥R⊙(⊃↙↘2)       # next coord by rotating x times
Valid ← /↧[⊃⊓(<W|<H)∩≥₀°⊟] # valid coordinate
Check ← ≠@#⍣⊡@.≡↘₂         # check neighbours not #

Neis ← (
  [⊃(N0|N1|N2|N3)] # neighbours
  ▽⤚Check          # keep unobstructed positions
)
FindPath ← (
  ⊂[¯1 0]⊢⊚⊸⌕@^ # start pos and direction
  °□⊢ astar(
    1¤⊢Neis  # neighbours with no rotation = lowest cost
  | 0        # heuristic of 0
  | ¬Valid↘₂ # keep going until out of grid
  )
  ⊙◌  # discard the cost
  ↘¯1 # discard last position which is outside the grid
)
IsLoop ← (
  ⍣(⋅0FindPath)1 # try to find a path out, else its a loop
)

# Part A
◴≡↘₂FindPath Input # unique path positions
⟜(&p⧻)             # count (keep positions for part B)

# Part B
≡⍜⊡⋅@#⊙[Input] # put obstacles in each part A position
↘1             # but not starting position
&p/+≡IsLoop    # sum up the loops
