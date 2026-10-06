import sys
import typing


def open_file(
        open_file_name: str,
        open_file_mode: str
) -> typing.IO[str] | None:
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
    except IsADirectoryError:
        print(f"Error opening file '{open_file_name}': "
              f"[Errno 21] Is a directory: '{open_file_name}'\n")
    return None


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
        if opened is None:
            return

        try:
            print(f"Reading data from '{file_to_open}'")
            data = opened.read()
            print(f"Data read from file '{file_to_open}'.")
        except UnicodeDecodeError:
            print(f"Error reading data from file '{file_to_open}': "
                  f"[Errno 0] Unicode decode error: '{file_to_open}'\n")
        finally:
            if not opened.closed:
                opened.close()
                footer(file_to_open)


if __name__ == "__main__":
    main()
