~ "../helpers/input.ua"
  ~ ReadInput
  ~ ReadSample

Input ← (
  ReadSample "day_12"
  ⊜∘≠,@\n
)

Ns ← [∩¯,,⇌.⇡2]     # neighbouring squares
G  ← ⊜□:⇡△.-@\0     # Groups
Nc ← ≡⬚@.⊡⊙¤≡(+Ns¤) # neighbouring chars
P  ← /+♭≠⊃(⊡⊢|Nc)   # Perimeter is uncovered squares

# Part A
Input
⊃G¤        # get the groups
⊃≡◇⧻≡(P°□) # get sizes & perimeters
/+×        # multiply sizes by perimeters & sum
