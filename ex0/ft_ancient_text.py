import sys
import typing

def open_file(
        open_file_name: str,
        open_file_mode: str
):
    try:
        print(f"Accessing file '{open_file_name}'")
        f = open(open_file_name, open_file_mode)
        return f
    except FileNotFoundError:
        print(f"Error opening file '{open_file_name}': "
        f"[Errno 2] No such file or directory: '{open_file_name}'\n")
    except PermissionError:
        print(f"Error opening file '{open_file_name}': "
        f"[Errno 13] Permission denied: '{open_file_name}'\n")


def header() -> None:
    print("=== Cyber Archives Recovery ===")


def footer(file_name: str) -> None:
    print("\n---\n"
    f"File '{file_name}' closed.")


def main() -> None:
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            print("[TOO MANY FILES] Wrong number of files: " 
                  "Usage: ft_ancient_text.py <file>\n")
        else:
            print("Usage: ft_ancient_text.py <file>\n")

    else:
        header()
        file_to_open = sys.argv[1]
        opened = open_file(file_to_open, "r")
        if not opened:
            return
        print("---\n")
        data = opened.read()
        print(data)
        opened.close()
        footer(file_to_open)


if __name__ == "__main__":
    main()
