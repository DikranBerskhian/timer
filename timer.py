import time
import sys


def get_input():
    while True:
        try:
            user_input = input("Write time to countdown (example: 0:5:55): ").strip()
            if not user_input:
                print("Please enter a time.")
                continue

            parts = user_input.split(":")
            if len(parts) != 3:
                print("Please use the format h:m:s (example 0:5:55)")
                continue

            if not all(p.isdigit() for p in parts):
                print("Use only positive numbers (no letters, symbols or negative numbers)")
                continue

            h, m, s = map(int, parts)
            if h < 0 or m < 0 or s < 0:
                print("Negative numbers are not allowed.")
                continue

            total = h * 3600 + m * 60 + s
            if total == 0:
                print("Time must be greater than 0.")
                continue

            return total

        except KeyboardInterrupt:
            print("\nGoodbye!")
            sys.exit(0)
        except Exception:
            print("Invalid input. Please try again.")


def run_countdown(total_seconds):
    while total_seconds >= 0:
        hours = total_seconds // 3600
        minutes = (total_seconds % 3600) // 60
        seconds = total_seconds % 60

        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        time.sleep(1)
        total_seconds -= 1

    print("Time is up!!!")


total = get_input()
run_countdown(total)