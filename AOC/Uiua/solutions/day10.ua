# Experimental!
Input ← (
  &fras "./data/day10.txt"
  ⊜∵⋕≠,@\n # convert to number grid
)

W      ← ⧻⊢Input
H      ← ⧻Input
Valid  ← /↧[⊃⊓(<W|<H)∩≥₀]°⊟ # is point within grid
Moves  ← ▽⊸≡Valid+⊙¤        # get valid neighbouring moves round a point
Nbrs ← (
  [∩¯,,⇌.⇡2]    # each direction
  ⊃(⟜⊡Moves|⋅⊡) # get grid values at current coord and valid moves
  ▽:⊙(=1-:)     # keep moves which are 1 increase
)
Trails ← (
  astar(
    Nbrs # Neighbours have equal cost
  | 0    # heuristic of 0
  | =9⊡  # keep going until finding a 9
  )
  ⊙◌ # discard cost
)
Score! ← (
  Input       # grid
  ⊃(⊚⌕0|¤)    # find trail start positions (coords of 0s)
  ≡(^0Trails) # for each one use the score function
  /+          # sum total score
)

# Part A
Score!(⧻◴⍚⊣) # score trails by unique end positions

# Part B
Score!⧻ # score trails by number of them
