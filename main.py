"""
This is a program to guide you through the game "Keep Talking and Nobody Explodes" by Steel Crate Games.
It assumes some prior knowledge of the game itself.
"""

# TODO add separate functions for: (simon_says, whos_on_first, memory, morse_code, complicated_wires, wire_sequences, mazes, passwords)


class indicator:
    """An indicator label on a bomb"""
    def __init__(self, isPresent: bool, isLit: bool, asked: bool) -> None:
        self.isPresent = isPresent
        self.isLit = isLit
        self.asked = asked


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


def int_getter(s: str, lim: int = None) -> int:
    try:
        ans = int(input(f"\n{s}\n"))
    except ValueError:
        print("\nPlease enter a valid integer!\n")
        ans = int_getter(s)


    if (lim is not None) and (ans > lim):
        print(f"Please enter a valid integer up to {lim}.")
        ans = int_getter(s, lim)

    return ans


def bool_getter(s: str) -> bool:
        print("\nPlease enter 'y' or 'yes' (without quotation marks) for a yes (anything else will be regarded as no).")
        ans = input(f"\n{s}\n")
        return ans.strip().lower() in ("y", "yes")


class modules:
    def __init__(self, indicators: dict, ports: dict, ser: serial, batteries: int) -> None:
        self.indicators = indicators
        self.ports = ports
        self.ser = ser
        self.batteries = batteries
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

            m = int_getter("Which module:")

            print(self.function_mappings[self.main_modules[m]]())

            if bool_getter("Would you like to continue?"):
                continue
            break

    def indicator_checker(self, indicator: str) -> None:
        if not self.indicators[indicator].asked:
            ans = bool_getter(f"Is there an indicator with the label '{indicator}' (without the quotation marks)?")
            if ans:
                self.indicators[indicator].isPresent = True
                ans = bool_getter(f"Is the indicator labelled '{indicator}' (without the quotation marks) lit?")
            if ans:
                self.indicators[indicator].isLit = True
            self.indicators[indicator].asked = True
            return False

    def wires(self) -> str:
        while True:
            how_many_wires = int_getter("How many wires are on the bomb?")

            if how_many_wires < 3:
                print("The minimum number of wires is 3!")
                continue
            elif how_many_wires > 6:
                print("The maximum number of wires is 6!")
                continue
            break

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
        button_held = True

        if self.batteries > 1:
            ans = bool_getter("Does the button say 'Detonate' (without the quotation marks)?")
            if ans:
                button_held = False

            elif self.batteries > 2:
                indicator = "FRK"
                self.indicator_checker(indicator)
                if self.indicators[indicator].isPresent and self.indicators[indicator].isLit:
                    button_held = False

            else:
                ans = bool_getter("Is the button red?")
                if ans:
                    ans = bool_getter("Does the button say 'Hold' (without the quotation marks)?")
                if ans:
                    button_held = False


        if not button_held:
            return "\nPress and immediately release the button."

        print("Press and hold the button. A strip will light up next to it.")
        print("Pick the colour of the strip by entering the corresponding number to the colour:")

        colours = {1: "Blue", 2: "White", 3: "Yellow", 4: "Other"}
        colour_mappings = {"Blue": 4, "White": 1, "Yellow": 5, "Other": 1}

        for item, value in colours.items():
            print(f"{item}: {value}")

        colour = int_getter("Which colour:")

        return f"Release the button when the count-down timer has a {colour_mappings[colours[colour]]} in any position."

    def keypads(self) -> str:
        order = []
        all_columns = (('Ϙ', 'Ѧ', 'ƛ', 'Ϟ', 'Ѭ', 'ϗ', 'Ͽ'),
                       ('Ӭ', 'Ϙ', 'Ͽ', 'Ҩ', '☆', 'ϗ', '¿'),
                       ('©', 'Ѽ', 'Ҩ', 'Җ', 'Ԇ', 'ƛ', '☆'),
                       ('б', '¶', 'Ѣ', 'Ѭ', 'Җ', '¿', 'ټ'),
                       ('Ψ', 'ټ', 'Ѣ', 'Ͼ', '¶', 'Ѯ', '★'),
                       ('б', 'Ӭ', '҂', 'æ', 'Ψ', 'Ҋ', 'Ω'))
        all_symbols_tuple = ('Ͽ', 'ټ', 'Ҩ', '★', 'Ӭ', 'Ψ', 'Ͼ', '©', '҂',
                             'Ѭ', '¿', 'Җ', 'б', 'Ϙ', 'Ԇ', 'Ѧ', 'Ѽ', '¶',
                             'Ѯ', 'Ѣ', 'Ҋ', '☆', 'Ϟ', 'Ω', 'æ', 'ƛ', 'ϗ')
        symbols = dict(zip(range(1, 28), all_symbols_tuple))

        print("Please enter the corresponding number to the shapes that are on your keypad module.")
        for item, value in symbols.items():
            print(f"{item}: {value}")

        first_symbol = symbols[int_getter("First symbol:", 27)]
        second_symbol = symbols[int_getter("Second symbol:", 27)]
        third_symbol = symbols[int_getter("Third symbol:", 27)]
        fourth_symbol = symbols[int_getter("Fourth symbol:", 27)]

        columns = [
            column
            for column in all_columns
            if (first_symbol in column)
            and (second_symbol in column)
            and (third_symbol in column)
            and (fourth_symbol in column)
        ]

        order = [
            symbol
            for column in columns
            for symbol in column
            if symbol in (first_symbol, second_symbol, third_symbol, fourth_symbol)
        ]

        print("Press the buttons on the keypad in this order:")
        return "\n".join(order)

    def simon_says(self) -> str:
        strikes = int_getter("How many strikes?", lim=2)
        colours = {1: "Red", 2: "Yellow", 3: "Green", 4: "Blue"}
        colour_mappings = {"Red": 1, "Yellow": 2, "Green": 3, "Blue": 4}

        print("Enter the corresponding number to the colour shown:")
        for item, value in colours.items():
            print(f"{item}: {value}")

        if self.ser.contains_vowel:
            if strikes == 0:
                pass
            elif strikes == 1:
                pass
            else:
                pass
        else:
            if strikes == 0:
                pass
            elif strikes == 1:
                pass
            else:
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


def serial_getter(s: str) -> str:
    ser = input(f"\n{s}\n")

    if (len(ser) < 6) or (len(ser) > 6):
        print("Please enter a valid six-character serial number!")
        ser = serial_getter(s)

    try:
        int(ser[-1])
    except ValueError:
        print("Please enter a valid six-character serial number! The last digit must be an integer!")
        ser = serial_getter(s)

    return ser


def main():
    indicators = {"SND": indicator(False, False, False), "CLR": indicator(False, False, False), "CAR": indicator(False, False, False),
                  "IND": indicator(False, False, False), "FRQ": indicator(False, False, False), "SIG": indicator(False, False, False),
                  "NSA": indicator(False, False, False), "MSA": indicator(False, False, False), "TRN": indicator(False, False, False),
                  "BOB": indicator(False, False, False), "FRK": indicator(False, False, False)}

    ports = {"DVI-D": False, "Parallel": False,
             "PS/2": False, "RJ-45": False,
             "Serial": False, "Stereo RCA": False}

    ser = serial(serial_getter("\nWhat is the serial number (6 character string) of the bomb: "))

    batteries = int_getter("How many batteries are on the bomb (total)?")


    modules(indicators, ports, ser, batteries)

    print("\n\nExiting...")


if __name__ == "__main__":
    main()
