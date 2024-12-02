Data ← (
  &fras "./data/day02.txt"
  ⊜□≠,@\n   # split into lines
  ⍚(⊜⋕≠,@ ) # split each line into list of numbers
)

Inc     ← /↧↧⊃<₄>₀≡/-◫2 # increasing by increments of 1-3
Safe    ← ↥∩Inc⟜⇌       # if list or reverse are increasing
Subsets ← ≡⍜↻↘₁⊙¤°⊏     # subsets with 1 item removed

SafeRemoved ← ↥/↥≡Safe Subsets⟜Safe # if safe with removal

/◇+⍚Safe Data        # part A - safe lists
/◇+⍚SafeRemoved Data # part B - safe lists with removal
