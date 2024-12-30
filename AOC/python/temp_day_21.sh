init="$(uv run python -m solutions.day_21)"
best=${init:(-15)}

for i in $(seq 1 1000); do
  value="$(uv run python -m solutions.day_21)"
  number=${value:(-15)}
  if [[ $number -lt $best ]]; then
    best=$number
  fi
done

echo $best
