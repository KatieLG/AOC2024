Input ← (
  &fras "./data/day03.txt"
)

ProductsRegex ← "mul\\((\\d+),(\\d+)\\)" # matches multiplications
Match         ← ≡↘₁⬚@ regex              # get matches for a regex pattern
SumProducts ← (
  Match ProductsRegex # find multiplications
  ≡(×°⊟⋕)             # uncouple pairs and multiply them 
  /+                  # sum everything
)

# Part A
Input
SumProducts

# Part B
Input             # get data
¬⦷"do()".         # mark by do() for group partition
⊜(▽\×¬⌕"don't()". # drop from first don't() onwards for each group
  SumProducts
)
/+
