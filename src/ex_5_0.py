"""ex_5_0.py"""


def line_count(infile):
    pass
# ex_5_0.py

def line_count(infile):
    try:
        with open(infile, 'r') as file:
            lines = file.readlines()
            num_lines = len(lines)
            print(f"The file '{infile}' has {num_lines} line(s).")
    except FileNotFoundError:
        print(f"Error: The file '{infile}' was not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Optional entry point for testing
if __name__ == "__main__":
    # Replace 'your_test_file.txt' with the actual file you want to test
    test_file = 'your_test_file.txt'
    line_count(test_file)


if __name__ == "__main__":
    # get the utility function for path discovery
    try:
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root

    # Test line_count with a file from the data directory
    data_directory = get_repository_root() / "data"
    line_count(data_directory / "ex_5_2-data.csv")
