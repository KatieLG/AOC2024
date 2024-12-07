Parse ← ⊜⍣⋕(□⊜⋕≠,@ )≠,@: # parse line
Input ← (
  &fras "./data/day07.txt"
  ▽≠,@\r
  ⊜Parse≠,@\n
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
