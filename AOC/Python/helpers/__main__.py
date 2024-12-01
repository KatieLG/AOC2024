import argparse
from argparse import Namespace
from datetime import datetime

from helpers.generate_files import generate_initial_files, generate_sample


def generate(args: Namespace) -> None:
    """Generate files within the month of december"""
    today = datetime.today()
    if not (today.year == 2024 and today.month == 12):
        raise ValueError("File generation only works during December 2024")
    for day in args.day or range(1, today.day + 1):
        if 1 in args.part:
            generate_initial_files(day)
        if 2 in args.part:
            generate_sample(day, 2)


parser = argparse.ArgumentParser(description="AOC input data helper")
subparsers = parser.add_subparsers()

submit_parser = subparsers.add_parser(
    "fetch", help="Fetch and save sample data from the AOC website"
)
submit_parser.add_argument(
    "--day",
    type=int,
    nargs="*",
    default=[],
    choices=range(1, 25),
    help="day to fetch data for",
)
submit_parser.add_argument(
    "--part",
    type=int,
    nargs="*",
    default=[1],
    choices=[1, 2],
    help="which part of the problem to fetch data for",
)
submit_parser.set_defaults(func=generate)

if __name__ == "__main__":
    ns = parser.parse_args()
    ns.func(ns)
