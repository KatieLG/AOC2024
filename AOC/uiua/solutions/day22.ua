~ "../helpers/input.ua" ~ ReadInput

Input ← (
  ReadInput "day_22"
  ⊜⋕≠,@\n
)

Xor     ← °⋯⬚0≠∩⋯                     # bitwise or
Mp      ← ◿16777216 Xor               # Mix and prune
Process ← memo(Mp⊸×₂₀₄₈Mp⌊⊸÷₃₂Mp⊸×₆₄) # Process a secret
Bananas ← ⇌◿10[⍥⊸Process2001]         # bananas per secret
Diff    ← -∩↘₁⊸↻₋₁◿10                 # differences between bananas

# Part A
Input
/+⍥Process2000 # sum up after 2000 iterations of processing

# Part B
Input
⊸≡Diff≡Bananas     # get differences between banana sales
◴♭₂≡(⧈∘4).⊙¤       # find the unique length 4 difference tuples
≡(/+≡⍣(⊡+4⊢⊚)0⌕)⊙¤ # find the sum of sales for each tuple
/↥                 # take the best one
