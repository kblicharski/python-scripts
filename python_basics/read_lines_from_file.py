import sys


def read_raw_file_contents(file: str) -> [str]:
    """Open a file and read its raw contents into a list."""
    with open(file) as f:
        return [line for line in f.readlines()]

def remove_certain_lines(raw_lines: [str]) -> [str]:
    """Remove lines that consist of all caps or blank lines."""
    return [line.strip() for line in raw_lines if line and line.islower()]

try:
    contents = read_raw_file_contents(sys.argv[1])
    print(contents)
    clean_contents = remove_certain_lines(contents)
    print(clean_contents)
except Exception:
    print('Malformed input, please try again.')
