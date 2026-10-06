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
    except FileNotFoundError as error:
        sys.stderr.write(f"[STDERR] Error opening file '{open_file_name}': "
                         f"{error}\n")
    except PermissionError as error:
        sys.stderr.write(f"[STDERR] Error opening file '{open_file_name}': "
                         f"{error}\n")
    except IsADirectoryError as error:
        sys.stderr.write(f"[STDERR] Error opening file '{open_file_name}': "
                         f"{error}\n")
    except UnicodeDecodeError as error:
        sys.stderr.write(f"[STDERR] Error opening file '{open_file_name}': "
                         f"{error}\n")
    return None


def save_file(file_name: str, data: str) -> None:
    opened = open_file(file_name, "w")
    if opened is None:
        return

    try:
        print(f"Saving data to '{file_name}'")
        opened.write(data)
        print(f"Data saved in file '{file_name}'.")
    except IsADirectoryError as error:
        sys.stderr.write(f"[STDERR] Error saving data to file '{file_name}': "
                         f"{error}\n"
                        )
    except EOFError as error:
        sys.stderr.write(f"[STDERR] Error saving data to file '{file_name}': "
                         f"{error}\n"
                        )
    finally:
        if not opened.closed:
            opened.close()


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
              "Usage: ft_stream_management.py <file>\n")
    else:
        print("Usage: ft_stream_management.py <file>\n")


def get_output_file_name() -> str:
    sys.stdout.write("Enter new file name (or empty): ")
    sys.stdout.flush()

    return sys.stdin.readline().strip()


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
        print("---")
        print(new_data)
        print("---")

        new_file_name = get_output_file_name()

        if new_file_name == "":
            print("Not saving data.")
            return

        save_file(new_file_name, new_data)


if __name__ == "__main__":
    main()
