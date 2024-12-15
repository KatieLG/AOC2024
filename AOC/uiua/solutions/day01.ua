~ "../helpers/input.ua" ~ ReadInput

Data ← (
  ReadInput "day_01"
  ⊜(⊜⋕≠,@ )≠,@\n # split on newlines & spaces per line
)

A ← ⊡0⍉Data # first col
B ← ⊡1⍉Data # second col

# part A
/+⌵-⍆A ⍆B # sum of the differences of sorted items

# part B
/+♭⊞(×⟜=)A B # sum of items in A x by their occurences in B
