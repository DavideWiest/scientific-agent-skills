#!/usr/bin/env -S uv run --script
#
# /// script
# dependencies = ["matplotlib>=3.8"]
# ///
"""Small CSV-to-figure helper for quick paper-like plots."""

from __future__ import annotations

import argparse
import csv
from pathlib import Path


def read_series(path: Path, x_name: str, y_names: list[str]) -> tuple[list[float], dict[str, list[float]]]:
    xs: list[float] = []
    ys = {name: [] for name in y_names}
    with path.open(newline="") as handle:
        reader = csv.DictReader(handle)
        for row in reader:
            xs.append(float(row[x_name]))
            for name in y_names:
                ys[name].append(float(row[name]))
    return xs, ys


def main() -> None:
    parser = argparse.ArgumentParser(description="Plot one or more numeric CSV columns.")
    parser.add_argument("csv", type=Path)
    parser.add_argument("--x", required=True, help="CSV column for the x axis")
    parser.add_argument("--y", required=True, nargs="+", help="CSV column(s) for the y axis")
    parser.add_argument("--out", required=True, type=Path, help="Output path, e.g. figure.pdf")
    parser.add_argument("--title", default="")
    parser.add_argument("--xlabel", default="")
    parser.add_argument("--ylabel", default="")
    parser.add_argument("--style", type=Path, default=Path(__file__).resolve().parents[1] / "assets" / "paper.mplstyle")
    parser.add_argument(
        "--transparent",
        action="store_true",
        help="Save with a transparent background for use in papers, slides, or websites.",
    )
    args = parser.parse_args()

    import matplotlib.pyplot as plt

    if args.style.exists():
        plt.style.use(args.style)

    xs, ys = read_series(args.csv, args.x, args.y)
    fig, ax = plt.subplots()
    for name, values in ys.items():
        ax.plot(xs, values, marker="o", label=name)

    ax.set_title(args.title)
    ax.set_xlabel(args.xlabel or args.x)
    ax.set_ylabel(args.ylabel or ", ".join(args.y))
    if len(args.y) > 1:
        ax.legend(frameon=False)

    args.out.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(args.out, transparent=args.transparent)


if __name__ == "__main__":
    main()
