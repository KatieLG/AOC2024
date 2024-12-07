Parse ← ⊜⍣⋕(□⊜⋕≠,@ )≠,@: # parse line
Input ← (
  &fras "./data/day07.txt"
  ▽≠,@\r
  ⊜Parse≠,@\n
)

Totals ← ≡⊢Input
Nums   ← ≡⊣Input
Apply! ← ≡⊂⊙¤^0°⊟⊃↙↘2 # Apply operations

Combinations₁ ← |1 (
  =1⊸⧻              # length of nums
  ⨬(Apply![⊃+×]     # get options for first two nums
    ♭≡Combinations₁ # Recursively make all totals
  | ⊢               # output final total
  )                 # possible combinations
)
Combinations₂ ← |1 (
  =1⊸⧻
  ⨬(Apply![⊃(+|×|⍜∩°⋕⊂)] # same again with join option
    ♭≡Combinations₂
  | ⊢
  )
)

# Part A
Totals
Nums
/◇+⍚×⊸⍚(∈Combinations₁)

# Part B
Totals
Nums
/◇+⍚×⊸⍚(∈Combinations₂)
