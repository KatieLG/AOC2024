~ "../helpers/input.ua" ~ ReadInput

Input ← (
  ReadInput "day_20"
  ⊜∘≠,@\n
)

Start ← ⊢⊚⌕@SInput          # start position
End   ← ⊢⊚⌕@EInput          # end position
Ns    ← ▽≠@#:⟜⊡+A₂¤         # valid neighbours
Solve ← ⊢path(Ns|≍End)Start # solve maze
Saving! ← (
  ⊃(/+⌵-∩↘₁|⌵-∩⊢)°⊟ # det grid distance and score distance
  -∩×⟜:⊸≤^0         # only keep the savings for cheat lengths under the threshold
)
SolutionPath ← Solve Input

Cheats! ← (
  ≡⊂°⊏          # add distances to solution path
  ⧅<2           # for each pair of coordinates on the path
  ♭≡(Saving!^0) # what is the saving
)

# Part A
SolutionPath
Cheats!2 # get cheats of length at most 2
/+≥100   # count how many are >= 100

# Part B
SolutionPath
Cheats!20 # get cheats of length at most 20
/+≥100    # count how many are >= 100
