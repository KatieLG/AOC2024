~ "../helpers/input.ua" ~ ReadInput

Match ← /◇⊂⍚⋕♭regex "\\d+" # find numbers
Input ← (
  ReadInput "day_13"
  ⊜Match¬⦷"\n\n". # split by double newline
)

Cost ← (
  ⊃(▽|▽¬)◿2°⊏         # equations for machine
  ∩(×⊢)⊸◡:            # multiply each by coef of the other
  ÷°⊟↘₁-              # calculate b uses
  ⟜(÷⊃(⊢|-°⊟↘₁)⍜⊡₁×:) # calculate a uses
  ◡(↧∩(=0◿₁))         # if both integers
  ⨬(0|+×3:)           # 0 if unsolvable else 3*a+b
)

# Part A
Input # get matrix of equations
≡Cost # solve each row
/+    # sum total button presses

# Part B
Input                 # get matrix of equations
≡⍜↘₄(+10000000000000) # add offset
≡Cost                 # solve each row
/+                    # sum total button presses
