~ "../helpers/input.ua" ~ ReadInput

Input ← (
  ReadInput "day_18"
  ⊜(⊜⋕≠,@,)≠,@\n
)

Fall ← 1024           # how many bytes have fallen
D    ← 71_71          # grid dimensions
Grid ← °⊚↙Fall Input  # form grid
Ns   ← [∩¯,,⇌.⇡2]     # neighbouring squares
VC   ← /↧↧⊃(<D|≥0_0)  # valid coords
VG   ← =0⊡            # valid in grid
Nbrs ← ▽:⟜VG▽⊸≡VC+Ns¤ # valid neighbours

Grid
path(
  Nbrs
| ≍-1D
)0_0

-1⧻⊢
