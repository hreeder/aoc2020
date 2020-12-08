from pathlib import Path

INPUTS = Path(__file__).parent.parent.parent / "inputs"


def load(day: int):
    with open(INPUTS / f"day{day}.txt") as df:
        day_n_input = df.read()

    return day_n_input
