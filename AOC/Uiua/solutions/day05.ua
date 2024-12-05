Input ← (
  &fras "./data/day05.txt"
  ⊜□¬⦷"\n\n". # split by double newline
)

S‼!     ← ⊜(^0⊜^1≠,^2)≠,@\n°□ # split by newlines then char
Rules   ← S‼!∘⋕@|⊢Input       # ordering rules
Updates ← S‼!□⋕@,⊣Input       # page updates

ValidRule    ← ↥⊃(≠2/+∈:|≥°⊟⊗)   # check if a rule is valid
Middle       ← ⊡⌊÷2⊸⧻            # middle element of array
ValidUpdates ← ⍚(/↧≡ValidRule:¤) # all valid updates

# Part A
¤Rules
Updates
⟜ValidUpdates # Get valid ones
/◇+⍚(×Middle) # sum up middle elements
