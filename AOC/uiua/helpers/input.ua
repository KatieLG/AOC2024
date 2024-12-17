ReadInput ← (
  &fras $"../data/_/dataset.txt" # read data
  ▽≠,@\r                         # remove any carriage returns
)

ReadSample ← (
  &fras $"../data/_/sample\_part\_one.txt" # read data
  ▽≠,@\r                                   # remove any carriage returns
)
