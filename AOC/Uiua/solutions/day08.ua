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
Antinodes ← (
  ◡-°⊟    # get differences
  [⊓-+⟜:] # go either side for antinodes
)

# Part A
Beacons
⍚(Coords          # find all coords
  ♭₂≡Antinodes⧅<2 # find antinodes
  ▽⊸≡Valid        # keep valid ones
)
⧻◴/◇⊂ # count up the unique antinodes
