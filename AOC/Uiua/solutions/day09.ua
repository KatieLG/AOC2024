Input ← &fras "./data/day09.txt"

Parse ← (
  ∵⋕           # convert to numbers
  ⊃(◿₂|⌊÷2)°⊏  # get file vs empty and ids
  ▽:⨬(⊢°⋕|⋅@.) # keep the correct number of each
)
Group      ← ⊜□+1⊛.
GroupLen   ← ⊜⧻+1⊛.
Compact    ← ⍜⊏⇌⊸[⊃(/↥⊚≠@.|⊗@.)] # one compacting step
NotCompact ← /↥⌕@./◇⊂↘₋₁Group    # are dots at the end
Checksum   ← /+×°⊏∵⋕▽≠,@.

# Part A
Parse Input
⍢(Compact|NotCompact) # Keep compacting while not compact
Checksum
