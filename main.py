"""
This is a program to guide you through the game "Keep Talking and Nobody Explodes" by Steel Crate Games.
It assumes some prior knowledge of the game itself.
"""

# TODO add separate functions for all the modules


class indicator:
    """An indicator label on a bomb"""
    def __init__(self, isPresent: bool, isLit: bool) -> None:
        self.isPresent = isPresent
        self.isLit = isLit


class serial:
    """The six-character long serial number on a bomb"""
    def __init__(self, number: str) -> None:
        self.number = number.lower()
        self.last_digit_even = self.last_digit_even_check()
        self.contains_vowel = self.contains_vowels_check()

    def last_digit_even_check(self) -> bool:
        l_digit = int(self.number[-1])
        return l_digit % 2 == 0

    def contains_vowels_check(self) -> bool:
        for vowel in ("a", "e", "i", "o", "u"):
            if vowel in self.number:
                return True


def int_getter(s: str) -> int:
    while True:
        try:
            ans = int(input(f"\n{s}\n"))
        except ValueError:
            print("\nPlease enter a valid integer!\n")
            continue
        return ans


def bool_getter(s: str) -> bool:
        print("\nPlease enter 'y' or 'yes' (without quotation marks) for a yes (anything else will be regarded as no).")
        ans = input(f"\n{s}\n")
        return ans.strip().lower() in ("y", "yes")


class module:
    def __init__(self, name: str, func: callable, args: list) -> None:
        self.name = name
        self.func = func
        self.args = args


def wires(serial_number: serial):
    how_many_wires = int_getter("How many wires are on the bomb?")

    if how_many_wires == 3:
        ans = bool_getter("Are there any red wires?")
        if ans:
            return "\nCut the second wire."

        ans = bool_getter("Is there more than one blue wire?")
        if ans:
            return "\nCut the last blue wire."

        return "\nCut the last wire."
    elif how_many_wires == 4:
        if not serial_number.last_digit_even:
            ans = bool_getter("Is there more than one red wire?")
            if ans:
                return "\nCut the last red wire."

        ans = bool_getter("Is the last wire yellow?")
        if ans:
            ans = bool_getter("Are there any red wires?")
        if ans:
            return "\nCut the first wire."

        ans = bool_getter("Is there ONLY ONE blue wire?")
        if ans:
            return "\nCut the first wire."

        ans = bool_getter("Is there more than one yellow wire?")
        if ans:
            return "\nCut the last wire."

        return "\nCut the second wire."
    elif how_many_wires == 5:
        if not serial_number.last_digit_even:
            ans = bool_getter("Is the last wire black?")
            if ans:
                return "\nCut the fourth wire."

        ans = bool_getter("Are there any black wires?")
        if not ans:
            return "\nCut the second wire."

        return "\nCut the first wire."
    else:
        if not serial_number.last_digit_even:
            ans = bool_getter("Are there any yellow wires?")
            if not ans:
                return "\nCut the third wire."

        ans = bool_getter("Are there any red wires?")
        if not ans:
            return "\nCut the last wire."

        return "\nCut the fourth wire."


def main():

    indicators = {"SND": indicator(False, False), "CLR": indicator(False, False), "CAR": indicator(False, False),
                  "IND": indicator(False, False), "FRQ": indicator(False, False), "SIG": indicator(False, False),
                  "NSA": indicator(False, False), "MSA": indicator(False, False), "TRN": indicator(False, False),
                  "BOB": indicator(False, False), "FRK": indicator(False, False)}

    ports = {"DVI-D": False, "Parallel": False,
             "PS/2": False, "RJ-45": False,
             "Serial": False, "Stereo RCA": False}

    ser = serial(input("\nWhat is the serial number (6 character string) of the bomb: "))

    main_modules = {1: module("Wires", wires, [ser]), 2: module("Button", None, []),
                    3: module("Keypads", None, []), 4: module("Simon Says", None, []),
                    5: module("Who's on First", None, []), 6: module("Memory", None, []),
                    7: module("Morse Code", None, []), 8: module("Complicated Wires", None, []),
                    9: module("Wire Sequences", None, []), 10: module("Mazes", None, []),
                    11: module("Passwords", None, [])}

    while True:
        print("\nPlease pick one of the modules to solve using the corresponding number:")
        for item, value in main_modules.items():
            print(f"{item}: {value.name}")

        m = int_getter("Which module: ")

        print(main_modules[m].func(*main_modules[m].args))
        break


if __name__ == "__main__":
    main()
