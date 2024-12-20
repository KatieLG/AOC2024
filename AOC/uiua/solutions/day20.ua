~ "../helpers/input.ua" ~ ReadInput

Input ← (
  ReadInput "day_20"
  ⊜∘≠,@\n
)

Start  ← ⊢⊚⌕@SInput        # start position
End    ← ⊢⊚⌕@EInput        # end position
Ns     ← ▽≠@#:⟜⬚@#⊡+A₂¤    # valid neighbours
Solve  ← -1⧻⊢path(Ns|≍End) # seconds to solve
Cheats ← ≡⍜⊡⋅@.⊚=@#⟜¤      # generate all possible cheats

Input
≡(Solve Start) Cheats # get the cheat times
-⟜/↥                  # compared to the normal time
⧻▽⊸≥₁₀₀               # how many save at least 100 seconds
