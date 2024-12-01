# AOC 2024

2024 Advent of Code solutions in python.

## Setup
Put AOC cookie in `.env` for pulling down the input data

## Usage

This contains a CLI to fetch and save the input data and scrape the sample data of the AOC website.
Usage is as follows:

Fetch input data, part one sample data and create a boilerplate python file for the current day:
```bash
make today
```

If sample data for part 2 differs from part 1, to scrape the part 2 data run:
```bash
make today-p2
```

For more granular use of the CLI for a specific day, the commands are:
```bash
python helpers fetch --day <day> --part <part>
```

## Formatting and Linting

Formatting and linting is done with ruff and can be run with
```bash
make lint
```

## Tests

Tests will run up to the current day of the month in December checking the outputs of given AOCSolution against the dictionary data in the class.
```bash
make test
```