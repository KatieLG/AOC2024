~ "../helpers/input.ua" ~ ReadInput

Input ← (
  ReadInput "day_17"
  ⊜□≠,@\n
)
M ← ♭≡⋕regex"\\d+" # match digits

RA ← ⊢M⊢Input  # Register A
RB ← ⊢M⊡₁Input # Register B
RC ← ⊢M⊡₁Input # Register C
P  ← M⊣Input   # Program

Xor   ← °⋯⬚0≠∩⋯
Combo ← ⨬(∘|⊸⊡-₄)⊸>₃       # 0-3 literals, 4-7 registers
Ops   ← ⊏⊙P+⇡2             # get opcode and operand
Div!  ← ⍜^0◌:⌊÷⊙⊸⊢ⁿ:2Combo # division in register
Done  ← ≥⧻P                # pointer has reached the end
Opcode ← ⨬(
  Div!⊢             # adv 0 a=a//2**combo
| ⍜⊙⊡₁Xor           # bxl 1 b=b^operand
| ⍜⊡₁⋅∘:◿₈Combo     # bst 2 b=combo%8
| ⊙(⨬-₂⋅∘=₀)⟜⊢:     # jnz 3 jump if a not 0
| ⍜⊡₁⋅∘:⋅⊸(Xor°⊟↘₁) # bxc 4 b=b^c
| ⊙⊙⊂⊙::◿₈Combo     # out 5 print combo%8
| Div!⊡₁            # bdv 6 b=a//2**combo
| Div!⊣             # cdv 7 c=a//2**combo
)
Next ← (
  ⟜Ops   # get the next operation
  °⊟⊙::  # reorder stack 
  Opcode # execute the opcode
  +₂:    # flip and increment pointer
)
RunProgram ← (
  ⊙[]           # output array
  0             # pointer
  ⍢(Next|¬Done) # run until done
  ⋅⋅⇌           # return output array
)

# Part A
RunProgram [RA RB RC]
/$"_,_"

# Part B
[0 1] # valid
0     # index
⍢(+₁⟜(
    ¤↙⊙P-1¯                    # find program from -i onwards
    ◴♭⊞+⇡8×8:                  # get the possible options for a
    ▽:⟜≡(≍RunProgram⊂⊙[RB RC]) # keep valid ones
  )
| <⧻P)
⋅⊢ # return the first valid a value
