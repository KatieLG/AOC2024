Input ← &fras "./data/day09.txt"

Parse ← (
  ∵⋕          # convert to numbers
  ⊃(◿₂|⌊÷₂)°⊏ # get file or empty and ids
  ▽:⍥⋅∞       # keep for each (with infinity as dots)
)
Checksum ← /+×°⊏▽≠,∞

# Part A
Parse Input
⊸⊃(⊚⌕∞|⇌⊚¬⌕∞) # get number and dot positions
∩↙⟜:↧◡∩⧻      # match on length
∩↙⟜:⊢⊚◡<      # keep those that would be a backward move
⍜⊏⇌⊂⇌         # perform moves
Checksum
