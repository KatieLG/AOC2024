~ "../helpers/input.ua" ~ ReadInput

Input ← (
  ReadInput "day_11"
  ⊜⋕≠,@  # convert to numbers
)

Split ← ⋕[⊃↙↘]÷2⊸⧻°⋕                  # split via strings
Trans ← ♭[⨬(⨬×₂₀₂₄Split=₀◿₂⧻°⋕.)1⊸=₀] # transform a stone
Blink ← |2 memo(
  ⨬(⊙Trans    # transform stone once
    -1        # decrement blink counter
    /+≡Blink¤ # return total from blinking remaining number of times
  | ⋅⋅1       # return 1 if 0 blinks left
  )⊸=₀
)

# Part A
Input
≡Blink¤25 # blink 25 times
/+        # count stones

# Part B
Input
≡Blink¤75 # blink 75 times
/+        # count stones
