Match ← /◇⊂⍚⋕♭regex "-?\\d+" # find numbers
Input ← (
  &fras "./data/day14.txt"
  ⊜Match≠,@\n # split by newline
)
Pos ← ≡↙₂Input
Dir ← ≡↘₂Input
W   ← 101   # width
H   ← 103   # height
B   ← [W H] # bounds

Move ← ≡(◿B)+Pos×Dir  # Move some number of times
Disp ← ⬚0+↯[H W]0°⊚≡⇌ # display grid

# Part A
Move 100
≡(⌊÷2W⊙(⌊÷2H)(°⊟)          # get the quadrant thresholds
  [⊃(↧⊓<>|↧⊓<<|↧⊓><|↧⊓>>)] # do each comparison
)
/×≡/+⍉ # sum coords in each quadrant and take the product

# Part B
# saving stuff into pngs until one looks like a tree
⇡10000
∵(⊸Move
  Disp
  ▽⟜≡▽3 # upscale
  img "png"
  &fwa $"images/day14\__.png" :
)
