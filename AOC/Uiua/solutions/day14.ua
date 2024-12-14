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

Move   ← ≡(◿B)+Pos×Dir   # Move some number of times
Disp   ← ⬚0+↯[H W]0°⊚≡⇌  # display grid
Loc!   ← ◿^0+×⇡⊙(∩¤⊃⊣⊢⍉) # locations over a number of moves
Lines! ← (
  Loc!^0 1000 # Get locations over 1000 moves
  ≡(/↥⊕⧻.⍆)   # maximum amount lining up
  ⊚>30        # find where more than 30 line up
)
SP ← ⊃⊢(-°⊟↙2) # start and period

# Part A
Move 100
≡(⌊÷2W⊙(⌊÷2H)(°⊟)          # get the quadrant thresholds
  [⊃(↧⊓<>|↧⊓<<|↧⊓><|↧⊓>>)] # do each comparison
)
/×≡/+⍉ # sum coords in each quadrant and take the product

# Part B
# Want a position with lots of x and y overlap
Xdx ← ≡(⊏0_2)Input
Ydy ← ≡(⊏1_3)Input
SP Lines!W Xdx # Find start and period of x line ups
SP Lines!H Ydy # Find start and period of y line ups
◡(⊙:-⊙:        # xs - ys
  ∵(+×⊙:)⇡,    # continually adding period
  ⊢⊚=0◿:       # find overlap point 
)
+×⊙⋅⋅: # moves for christmas tree
