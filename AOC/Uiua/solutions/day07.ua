~ "../helpers/input.ua" ~ ReadInput

Parse ← ⊜⍣⋕(□⊜⋕≠,@ )≠,@: # parse line
Input ← (
  ReadInput "day_07"
  ⊜Parse≠,@\n # split on newlines and parse
)

Totals ← ≡⊢Input
Nums   ← ≡⊣Input

Combinations! ← (
  ⍚(×⊸∈♭/[^0]) # get all valid totals with operations
  /◇+          # sum them
)

# Part A
Totals
Nums
Combinations!⊃+× # combos with + and ×

# Part B
Totals
Nums
Combinations!⊃(+|×|∵⍜∩°⋕⊂) # with + and × and joining
