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


def save_file(file_name: str, data: str) -> None:
    opened = open_file(file_name, "w")
    if opened is None:
        return

    try:
        print(f"Saving data to '{file_name}'")
        opened.write(data)
    except IsADirectoryError:
        print(f"Error saving data to file '{file_name}': "
              f"[Errno 21] Is a directory: '{file_name}'\n")
    except EOFError:
        print(f"Error saving data to file '{file_name}': "
              f"[Errno 0] EOF error: '{file_name}'\n")
    except OSError as error:
        print(f"Error saving data to file '{file_name}': "
              f"{error}\n")
    finally:
        if not opened.closed:
            opened.close()
            print(f"Data saved in file '{file_name}'.")



def transform_data(data: str) -> str:
    lines = data.splitlines()
    transformed_lines = []

    for line in lines:
        transformed_lines.append(line + "#")

    return "\n".join(transformed_lines)


def header() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")


def footer(file_name: str) -> None:
    print("\n---\n"
          f"File '{file_name}' closed.")


def argv_error() -> None:
    if len(sys.argv) > 2:
        print("[TOO MANY FILES] Wrong number of files: "
              "Usage: ft_archive_creation.py <file>\n")
    else:
        print("Usage: ft_archive_creation.py <file>\n")


def main() -> None:
    if len(sys.argv) != 2:
        argv_error()
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
            print("---")
            print(data)
        except (OSError, UnicodeDecodeError) as error:
            print(f"Error reading file '{file_to_open}': {error}")
            return
        finally:
            if not opened.closed:
                opened.close()
                footer(file_to_open)

        new_data = transform_data(data)
        print("Transform data:")
        print("---")
        print(new_data)
        print("---")

        try:
            new_file_name = input("Enter new file name (or empty): ")
        except EOFError:
            print("\nInput ended. Data not saved.")
            return

        if new_file_name == "":
            print("Not saving data.")
            return

        save_file(new_file_name, new_data)


if __name__ == "__main__":
    main()
