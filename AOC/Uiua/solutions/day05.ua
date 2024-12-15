~ "../helpers/input.ua" ~ ReadInput

Input ← (
  ReadInput "day_05"
  ⊜□¬⦷"\n\n". # split by double newline
)

S‼!     ← ⊜(^0⊜^1≠,^2)≠,@\n°□ # split by newlines then char
Rules   ← S‼!∘⋕@|⊢Input       # ordering rules
Updates ← S‼!□⋕@,⊣Input       # page updates

ValidRule   ← ↥⊃(≠2/+∈:|≥°⊟⊗)     # is rule valid for update
ValidUpdate ← /↧≡ValidRule Rules¤ # is update valid
Middle      ← ⊡⌊÷2⊸⧻              # middle element of array

Fix ← (
  ◡≡ValidRule Rules¤ # check rules
  ⊡⊗0                # pick the first invalid one
  ⍜⊏⇌⊸⊗⊙♭            # swap elements round
)

# Part A
Updates
⟜⍚ValidUpdate # Get valid ones
/◇+⍚(×Middle) # sum up middle elements

# Part B
Updates
⟜(¬⍚ValidUpdate)     # Get invalid ones
▽∵°□:                # keep them
⍚⍢(Fix|¬ValidUpdate) # Fix until valid
/◇+⍚Middle           # sum up middle elements
