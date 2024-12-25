~ "../helpers/input.ua" ~ ReadInput

Parse ← ⊜∘≠,@\n
Input ← (
  ReadInput "day_25"
  ⊜Parse¬⦷"\n\n".
)

IsLock  ← /↥∊@#⊢
Heights ← ⊗@.⍉⍥⇌¬⊸IsLock
Fits    ← =1/↧≤7+∩Heights

# Part A
Input
⊃(▽⊸≡IsLock|▽¬⊸≡IsLock) # get locks and keys
/+♭⊞Fits                # count the pairs that fit
