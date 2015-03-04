#!/usr/bin/env python3
import argparse
import csv
import logging
import os

from PIL import Image


def image_to_csv(input_file):
    prefix, _ = os.path.splitext(input_file)
    output_file = prefix + ".csv"
    logging.debug("Converting %s to %s.", input_file, output_file)
    with Image.open(input_file) as image, \
            open(output_file, "x", newline="") as f:
        image = image.convert("1") # convert to black and white
        csv_writer = csv.writer(f)
        width, height = image.size
        for y in range(height):
            line = [1 if image.getpixel((x, y)) else 0 for x in range(width)]
            csv_writer.writerow(line)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("input_files", nargs="+")
    parser.add_argument("--verbose", "-v", action="store_true", default=False)
    args = parser.parse_args()

    level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(format='%(levelname)s: %(message)s', level=level)

    for input_file in args.input_files:
        image_to_csv(input_file)
