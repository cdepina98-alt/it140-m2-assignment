"""This program gathers information like names and ages to calculate
Then display their estimated year of birth.

Input:
    Using the keyboard, the user writes their name as text(string).
    Using the keyboard, the user writes their age as an integer.

Process:
    The program will subtract the user's age from the current year to
    calculate their estimated birth year.


Output:
    The Program displays the user's name and their estimated year of birth as
      text (string) on the screen.

Typical usage example:
    Enter your name: Jeremy
    Enter your age: 23
    Jeremy, you were born in 2003.
"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system as integer


# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input.
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    # Calculate user's approximate birth year.
    birth_year = CURRENT_YEAR - age

    # Output personalized message with user's name and birth year.
    print(f"{name}, you were born in {birth_year}.")


# === Main Guard ===
if __name__ == "__main__":
    main()


# === References ===
