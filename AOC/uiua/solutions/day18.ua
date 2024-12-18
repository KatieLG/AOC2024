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

Solve ← (
  0_0 # start at 0_0
  ⊢path(
    Nbrs
  | ≍-1D # end on bottom right of grid
  )
  -1⧻ # steps taken for shortest path
)
Solvable ← (
  °⊚↙
  ⍣(⋅1Solve)0 # is the grid solvable 
)

# Part A
Input
°⊚↙1024 # 1024 bytes fall
Solve

# Part B
Input
1024            # start checking from 1024
⍢(+15|Solvable) # check in steps of 15
⍢(-1|¬Solvable) # narrow down to first problem byte
/$"_,_"⊡        # coordinates
