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
  ⊃(/+⌵-∩↘₁|⌵-∩⊢) # det grid distance and score distance
  -∩×⟜:⊸≤^0       # only keep the savings for cheat lengths under the threshold
)

Cheats! ← (
  .≡⊂°⊏ # add distances to solution path
  ⊞(
    ◡(≤∩□)         # filter to upper quadrant to avoid doubling cheats
    ⨬(0|Saving!^0) # get the savings for each pair
  )
  ♭
)

# Part A
Solve Input # get solution
Cheats!2    # get cheats of length at most 2
/+≥100      # count how many are >= 100

# Part B
Solve Input # get solution
Cheats!20   # get cheats of length at most 20
/+≥100      # count how many are >= 100
