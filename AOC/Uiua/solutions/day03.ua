Input ← (
  &fras "./data/day03.txt"
)

MultRegex   ← "mul\\((\\d+),(\\d+)\\)"
DoDontRegex ← "(do)\\(\\)|(don't)\\(\\)"

Include ← /↥∈□"do"
Exclude ← /↥∈□"don't"
Mult    ← /◇×⍚⍣⋕0↙2

# Part A
Input           # get data
regex MultRegex # find multiplications
/+≡(×°⊟⋕↘₁)     # sum them

# Part B
Input                                 # get data
⊂"do()"                               # start with do()
⬚@ regex $"_|_" MultRegex DoDontRegex # find mul/do/dont
≡(+⊃(Include|¯Exclude|Mult)↘₁)        # find enable/disable
>0\(⨬∘⋅∘≠0,)                          # mark products to keep
/+▽                                   # keep and sum
