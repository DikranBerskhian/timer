# ⏱️ Countdown Timer

A simple command-line countdown timer written in Python. Enter any duration in `h:m:s` format and watch it count down to zero — one second at a time.

---

## Features

- Accepts time input in `hours:minutes:seconds` format
- Validates input and gives clear error messages for invalid entries
- Displays the remaining time in `HH:MM:SS` format, updated every second
- Lightweight — uses only Python's built-in `time` module

---

## Requirements

- Python 3.6+

No external dependencies needed.

---

## Usage

```bash
python countdown.py
```

You'll be prompted to enter a duration:

```
Insert time to count down (h:m:s): 0:1:30
01:30
01:29
01:28
...
00:00:01
00:00:00
```

### Input format

| Input | Meaning |
|-------|---------|
| `1:0:0` | 1 hour |
| `0:5:0` | 5 minutes |
| `0:0:45` | 45 seconds |
| `1:30:0` | 1 hour and 30 minutes |

---

## Input Validation

The script handles the following invalid inputs gracefully:

| Issue | Example | Error message |
|-------|---------|---------------|
| Wrong format | `90` or `5-00` | `Invalid format. Please use h:m:s` |
| Non-numeric values | `a:b:c` | `Invalid input. Please enter whole numbers only.` |
| Negative values | `-1:0:0` | `Please enter non-negative values.` |
| Zero duration | `0:0:0` | `Please enter a time greater than zero.` |

---

## Project Structure

```
countdown.py   # Main script
README.md      # This file
```

---

## License

This project is free to use and modify.
