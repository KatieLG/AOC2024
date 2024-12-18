~ "../helpers/input.ua"
  ~ ReadInput
  ~ ReadSample

Input ← (
  ReadInput "day_12"
  ⊜∘≠,@\n
)

Ns    ← [∩¯,,⇌.⇡2]        # neighbouring squares
G     ← ⊜□:⇡△.-@\0        # Groups
Nc    ← ≡⬚@.⊡⊙¤≡(+Ns¤)    # neighbouring chars
P     ← /+♭≠⊃(⊡⊢|Nc)      # Perimeter is uncovered squares
Ps    ← ⊂↯⊙1⧻⊢.           # pad single grid border
Pad   ← Ps⍜(⇌⍉)Ps⍜⇌Ps⍜⍉Ps # pad whole grid
M     ← ≠@.⍜⊡≡⋅@.         # mask group in grid
S!    ← ≡(⧻⊜⧻.⊛⌕^0⍉)⧈∘2   # get sides for a row or col
Sides ← /+♭[⊃(S!1_0|S!0_1|S!1_0⍉|S!0_1⍉)]

# Part A
Input
⊃G¤        # get the groups
⊃≡◇⧻≡(P°□) # get sizes & perimeters
/+×        # multiply sizes by perimeters & sum

# Part B
Input
⊃G¤                  # get the groups
⊃≡◇⧻≡(Sides Pad M°□) # get sizes & sides
/+×                  # multiply sizes by sides & sum
