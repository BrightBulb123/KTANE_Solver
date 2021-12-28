"""
This is a program to guide you through the game "Keep Talking and Nobody Explodes" by Steel Crate Games.
It assumes some prior knowledge of the game itself.
"""

# TODO add separate functions for all the modules

def main():
    main_modules = {1: "Wires", 2: "Button", 3: "Keypads",
                    4: "Simon Says", 5: "Who's on First", 6: "Memory",
                    7: "Morse Code", 8: "Complicated Wires", 9: "Wire Sequences",
                    10: "Mazes", 11: "Passwords"}

    indicators = {"SND": {"isPresent": False, "isLit": False}, "CLR": {"isPresent": False, "isLit": False}, "CAR": {"isPresent": False, "isLit": False},
                  "IND": {"isPresent": False, "isLit": False}, "FRQ": {"isPresent": False, "isLit": False}, "SIG": {"isPresent": False, "isLit": False},
                  "NSA": {"isPresent": False, "isLit": False}, "MSA": {"isPresent": False, "isLit": False}, "TRN": {"isPresent": False, "isLit": False},
                  "BOB": {"isPresent": False, "isLit": False}, "FRK": {"isPresent": False, "isLit": False}}

    ports = {"DVI-D": False, "Parallel": False,
             "PS/2": False, "RJ-45": False,
             "Serial": False, "Stereo RCA": False}


if __name__ == "__main__":
    main()
