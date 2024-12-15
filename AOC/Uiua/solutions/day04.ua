~ "../helpers/input.ua" ~ ReadInput

Input ← (
  ReadInput "day_04" # input
  ⊜∘≠,@\n            # split on newlines
)

TD ← ⍉≡⬚@.↻⇡⧻.    # Top Left diagonals
LD ← ⊂⊃(TD|↘1TD⍉) # Top & Bottom Left diagonals
D  ← ⊂⊃(LD|LD≡⇌)  # Left & Right diagonals

Count ← (
  ⊃(⌕|⌕⇌) # find word or its reverse
  /+♭⊂    # total count
)

# Part A
Input
⊂⊂⟜⊃⍉D      # get rows, cols & diags
Count"XMAS" # count occurences of XMAS in each

# Part B
Input
♭₃⧈∘3_3          # get 3x3 windows 
≡(=2Count"MAS"D) # 2 occurences of MAS on diagonals = X-MAS    
/+               # total occurences
