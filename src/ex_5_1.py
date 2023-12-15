"""ex_5_1.py"""
try:
    from src.ex_5_0 import line_count
except ImportError:
    from ex_5_0 import line_count

import argparse


def main(infile):
    """Call line_count with the infile argument."""
    line_count(infile)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description='This program prints the number of lines in infile.')
    parser.add_argument('filename',
                        help='Filename to count the lines in it')
    args = parser.parse_args()
    main(args.filename)
 
