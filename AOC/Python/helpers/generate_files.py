import logging
import os
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

load_dotenv()

COOKIE = os.getenv("COOKIE")

if not COOKIE:
    raise EnvironmentError("An AOC COOKIE in your .env is required for this to run")

BASE_URL = "https://adventofcode.com/2024"
ROOT = Path(__file__).parent.parent.parent
HEADERS = {
    "Content-type": "application/json",
    "Accept": "text/html",
    "Cookie": COOKIE,
}
TEMPLATE = """from models.aoc_solution import AOCSolution


class Day<DAY>(AOCSolution):
    EXPECTED = {
        "part_one": {"sample": 0, "data": 0},
        "part_two": {"sample": 0, "data": 0},
    }

    def part_one(self) -> int:
        return 0

    def part_two(self) -> int:
        return 0


if __name__ == "__main__":
    Day<DAY>().run()

"""


def save_data(data: str, *, day: int, is_sample: bool = False, part: int = 1) -> None:
    """Saves sample/input data to file"""
    data = data.strip()
    data_path = Path(ROOT, f"data/day_{day:02d}")
    data_path.mkdir(exist_ok=True, parents=True)

    if is_sample:
        number = "one" if part == 1 else "two"
        file_path = Path(data_path, f"sample_part_{number}.txt")
    else:
        file_path = Path(data_path, "dataset.txt")

    file_path.write_text(data)
    logger.info(f"Successfully saved to {file_path}")


def generate_sample(day: int, part: int) -> None:
    """Scrape page from AOC website for the sample data. Assume it is the largest code block"""
    url = f"{BASE_URL}/day/{day}"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")
    code_blocks = [element.text for element in soup.find_all("code")]

    if not code_blocks:
        logger.warning(f"No code blocks found for day {day}")

    longest = max(code_blocks, key=len, default="")
    save_data(longest, day=day, is_sample=True, part=part)


def generate_data(day: int) -> None:
    """Fetches the input data for a given day from the AOC website"""
    url = f"{BASE_URL}/day/{day}/input"
    response = requests.get(url, headers=HEADERS)
    response.raise_for_status()

    input_data = response.text
    save_data(input_data, day=day)


def generate_initial_files(day: int) -> None:
    """
    Fetches sample and input data for a given day.
    Populates both part-1 and part-2 sample data with the longest code block,
    so if they are the same, no extra cli command is required
    """
    logger.info(f"Generating files for day {day}")

    python_path = Path(ROOT, f"python/solutions/day_{day:02d}.py")
    if not python_path.exists():
        python_path.write_text(TEMPLATE.replace("<DAY>", f"{day:02d}"))
        logger.info(f"Created solution file: {python_path}")

    generate_sample(day, part=1)
    generate_sample(day, part=2)
    generate_data(day)

    logger.info(f"Successfully generated all files for day {day}")
