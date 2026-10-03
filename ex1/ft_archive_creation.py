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
    return None


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

        print("---\n")

        data = opened.read()

        print(data)

        opened.close()
        footer(file_to_open)

        new_data = transform_data(data)
        print("Transform data:")
        print("---")
        print(new_data)
        print("---")

        new_file_name = input("Enter new file name (or empty): ")

        if new_file_name == "":
            print("Not saving data.")
            return
        
        opened = open_file(new_file_name, "w")
        if opened is None:
            return

        print(f"Saving data to '{new_file_name}'")
        opened.write(new_data)
        opened.close()
        
        print(f"Data saved in file '{new_file_name}'.")


if __name__ == "__main__":
    main()
