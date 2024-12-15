ReadInput ← (
  &fras $"../data/_/dataset.txt" # read data
  ▽≠,@\r                         # remove any carriage returns
)
