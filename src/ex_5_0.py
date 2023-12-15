def line_count(infile):
    with open(infile, 'r') as f:
        line = f.readlines()
    print(len(line))


if __name__ == "__main__":
  
    try:
        from src.util import get_repository_root
    except ImportError:
        from util import get_repository_root

   
    data_directory = get_repository_root() / "data"
    line_count(data_directory / "ex_5_2-data.csv")
   
