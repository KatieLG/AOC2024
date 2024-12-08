Input ← (
  &fras "./data/day08.txt"
  ▽≠,@\r  # remove carriage return
  ⊜∘≠,@\n # split on newlines
)

W       ← ⧻⊢Input        # width
H       ← ⧻Input         # height
Beacons ← ▽≠,@.◴/◇⊂Input # All beacon characters

Coords ← ⊚⌕⊙Input          # Find coords of beacon
Valid  ← ↧∩↧⊃⊓(<W|<H)∩≥₀°⊟ # is coord in grid
AN ← (
  ◡-°⊟    # get difference
  [⊓-+⟜:] # go either side for antinodes
)
DirectedAN ← (
  ×⊙(-°⊟⊸↙₂)            # get directed difference
  ⋅↘₁⍢(⊙⊂⟜+⊙⊸⊢|Valid⋅⊢) # keep adding until out of grid
)
AntinodeUnion! ← (
  ⍚(Coords   # find all coords
    ^0⧅<2    # find antinodes for each pair
    ▽⊸≡Valid # keep valid ones
  )
  ⧻◴/◇⊂ # count up the unique antinodes
)

# Part A
Beacons
AntinodeUnion!(♭₂≡AN)

# Part B
Beacons
AntinodeUnion!(
  ⍚(⊂⊃(DirectedAN1|DirectedAN¯1)) # nodes either side
  /◇⊂                             # joined up
)
