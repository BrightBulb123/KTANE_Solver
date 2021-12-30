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


class modules:
    def __init__(self, indicators: dict, ports: dict, ser: serial) -> None:
        self.indicators = indicators
        self.ports = ports
        self.ser = ser
        self.main_modules = {1: "Wires", 2: "Button",
                             3: "Keypads", 4: "Simon Says",
                             5: "Who's on First", 6: "Memory",
                             7: "Morse Code", 8: "Complicated Wires",
                             9: "Wire Sequences", 10: "Mazes",
                             11: "Passwords"}
        self.function_mappings = {"Wires": self.wires, "Button": self.button,
                                  "Keypads": self.keypads, "Simon Says": self.simon_says,
                                  "Who's on First": self.whos_on_first, "Memory": self.memory,
                                  "Morse Code": self.morse_code, "Complicated Wires": self.complicated_wires,
                                  "Wire Sequences": self.wire_sequences, "Mazes": self.mazes,
                                  "Passwords": self.passwords}

        while True:
            print("\nPlease pick one of the modules to solve using the corresponding number:")
            for item, value in self.main_modules.items():
                print(f"{item}: {value}")

            m = int_getter("Which module: ")

            print(self.function_mappings[self.main_modules[m]]())

            if bool_getter("Would you like to continue?"):
                continue
            break

    def keep_playing(self):
        return bool_getter("Would you like to continue?")

    def wires(self) -> str:
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
            if not self.ser.last_digit_even:
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
            if not self.ser.last_digit_even:
                ans = bool_getter("Is the last wire black?")
                if ans:
                    return "\nCut the fourth wire."

            ans = bool_getter("Are there any black wires?")
            if not ans:
                return "\nCut the second wire."

            return "\nCut the first wire."
        else:
            if not self.ser.last_digit_even:
                ans = bool_getter("Are there any yellow wires?")
                if not ans:
                    return "\nCut the third wire."

            ans = bool_getter("Are there any red wires?")
            if not ans:
                return "\nCut the last wire."

            return "\nCut the fourth wire."

    def button(self) -> str:
        pass

    def keypads(self) -> str:
        pass

    def simon_says(self) -> str:
        pass

    def whos_on_first(self) -> str:
        pass

    def memory(self) -> str:
        pass

    def morse_code(self) -> str:
        pass

    def complicated_wires(self) -> str:
        pass

    def wire_sequences(self) -> str:
        pass

    def mazes(self) -> str:
        pass

    def passwords(self) -> str:
        pass


def main():
    indicators = {"SND": indicator(False, False), "CLR": indicator(False, False), "CAR": indicator(False, False),
                  "IND": indicator(False, False), "FRQ": indicator(False, False), "SIG": indicator(False, False),
                  "NSA": indicator(False, False), "MSA": indicator(False, False), "TRN": indicator(False, False),
                  "BOB": indicator(False, False), "FRK": indicator(False, False)}

    ports = {"DVI-D": False, "Parallel": False,
             "PS/2": False, "RJ-45": False,
             "Serial": False, "Stereo RCA": False}

    ser = serial(input("\nWhat is the serial number (6 character string) of the bomb: "))


    game = modules(indicators, ports, ser)

    print("\n\nExiting...")


if __name__ == "__main__":
    main()
