*This project was created as part of the 42 curriculum by dswietoc.*

# Python Module 04 — Data Archivist

File operations and standard streams.

## Description

Exercises in reading, transforming, and saving text files, handling file errors, using standard streams, and managing file lifetimes explicitly and with context managers.

## Requirements

- Python 3.10 or later.
- No third-party packages are needed to run the exercises.
- `flake8` and `mypy` are optional development tools for linting and type checking.

## Setup

```bash
git clone https://github.com/doniu112/42_Python_Module_04.git
cd 42_Python_Module_04
```

The commands below use a Linux, macOS, or WSL shell and `python3`.

## Exercises

| Exercise | File | Purpose |
| --- | --- | --- |
| ex0 | [ft_ancient_text.py](ex0/ft_ancient_text.py) | Read and display a text file supplied on the command line. |
| ex1 | [ft_archive_creation.py](ex1/ft_archive_creation.py) | Append # to each text line and optionally save the result. |
| ex2 | [ft_stream_management.py](ex2/ft_stream_management.py) | Use stdin, stdout, and stderr explicitly. |
| ex3 | [ft_vault_security.py](ex3/ft_vault_security.py) | Provide secure_archive() using with and a structured result. |

## Usage

Run exercises 0-2 from the repository root using the supplied sample:

```bash
python3 ex0/ft_ancient_text.py ex0/ancient_fragment.txt
python3 ex1/ft_archive_creation.py ex0/ancient_fragment.txt
python3 ex2/ft_stream_management.py ex0/ancient_fragment.txt
```

Exercises 1 and 2 ask for an output filename. Press Enter to skip saving, or enter a path such as `archived_fragment.txt`. Saving creates the target or overwrites its existing contents.

Exercise 3 uses paths relative to the working directory. Run its demonstration from `ex3`:

```bash
cd ex3
python3 ft_vault_security.py
cd ..
```

The successful write demonstration creates or replaces `ex3/new_fragment.txt`. The `/etc/master.passwd` example is platform-dependent: it may report a missing file rather than a permission error.

## Implementation notes

- Exercises 0-2 open and close files explicitly. Exercise 3 introduces the `with` statement.
- Exercises 1 and 2 insert `#` at the end of each line before saving.
- Exercise 2 reads the destination through `sys.stdin.readline()` and sends exception details to `sys.stderr` with a `[STDERR]` prefix.
- The save helpers handle errors during writing and closing; success is reported only after both operations finish.
- `secure_archive(file_name, action="read", content="")` returns a `tuple[bool, str]`: a success flag and either file contents, a confirmation, or an error message.
- Supported actions for `secure_archive()` are `"read"` and `"write"`. An unsupported action returns `(False, "Invalid action")`.

## Code quality

Create a virtual environment and install the development tools:

```bash
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install flake8 mypy
```

From the repository root:

```bash
python3 -m flake8 ex*/*.py
python3 -m mypy --strict --explicit-package-bases ex*/*.py
```

Basic manual checks from the repository root:

```bash
python3 ex0/ft_ancient_text.py missing_file.txt
python3 ex0/ft_ancient_text.py ex0
python3 ex1/ft_archive_creation.py ex0/ancient_fragment.txt
```

The first two commands demonstrate file errors. In the third, test both skipping the save and writing to a disposable output file.

## Related modules

- [Module 00 — Growing Code](https://github.com/doniu112/42_Python_Module_00)
- [Module 01 — Code Cultivation](https://github.com/doniu112/42_Python_Module_01)
- [Module 02 — Garden Guardian](https://github.com/doniu112/42_Python_Module_02)
- [Module 03 — Data Quest](https://github.com/doniu112/42_Python_Module_03)

