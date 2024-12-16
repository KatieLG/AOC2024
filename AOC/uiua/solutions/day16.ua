~ "../helpers/input.ua" ~ ReadInput

Input ← (
  ReadInput "day_16"
  ⊜∘≠,@\n
)
Start ← ♭⊚⌕@SInput
End   ← ♭⊚⌕@EInput
Dir   ← [0 1]            # facing east
Rot!  ← ⊂:⊂^0⊃(⊡₃|⊡₂|↙₂) # rotation
Nbrs ← (
  ⟜(
    ⊂⊸+⊃↙↘2 # move forward with cost of 1
    ⊙⊡⊃⊂₁↙₂ # check it in grid
    ⊂≠@#:   # mark if valid
  )
  ⟜(⊂1_1000Rot!⊙¯) # rotate clockwise cost of 1000
  ⊂1_1000Rot!¯     # rotate counterclockwise for 1000
)
Moves ← (
  [Nbrs] # get neighbours
  ▽⊸≡⊢   # keep the valid ones
  ≡⊃⊡₁↘₂ # get new vectors + costs
)
Solve ← (
  path(
    Moves  # Pick from moves with costs
  | ≍End↙₂ # keep going until on the Ending
  )
)

# Part A
Input      # Grid
⊂Start Dir # Start position and start direction
◌Solve     # solve and discard paths for cost only

# Part A
Input      # Grid
⊂Start Dir # Start position and start direction
⊙◌Solve    # solve and discard cost for paths
⧻◴≡↙₂/◇⊂   # find all points that lie on a best path
