~ "../helpers/input.ua" ~ ReadInput

Input ← (
  ReadInput "day_19"
  ⊜□¬⦷"\n\n".
)

Patterns ← ⊜□≠,@,▽≠,@ °□⊢Input # available patterns
Designs  ← ⊜□≠,@\n°□⊣Input     # desired designs

Count ← |1 memo(
  ≠0⊸⧻
  ⨬(1                     # if design empty, return 1
  | ▽/◇⊂◡⍚(=1⊢⌕)Patterns¤ # find patterns design starts with
    °□/◇+⍚(Count↘⧻)       # count design[len(pattern):]
  )
)

# Part A
Designs
/◇+>₀⍚Count # Designs that have >0 arrangements

# Part B
Designs
/◇+⍚Count # Sum all possible arrangements
