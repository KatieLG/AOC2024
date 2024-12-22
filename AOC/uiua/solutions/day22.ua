~ "../helpers/input.ua" ~ ReadInput

Input ← (
  ReadInput "day_22"
  ⊜⋕≠,@\n
)

Xor     ← °⋯⬚0≠∩⋯               # bitwise or
Mp      ← ◿16777216 Xor         # Mix and prune
Process ← Mp⊸×₂₀₄₈Mp⌊⊸÷₃₂Mp⊸×₆₄ # Process a secret

# Part A
Input
/+⍥Process2000 # sum up after 2000 iterations of processing
