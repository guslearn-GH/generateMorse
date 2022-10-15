morseDict = {"A": "*-",
             "B": "-***",
             "C": "-*-*",
             "D": "-**",
             "E": "*",
             "F": "**-*",
             "G": "--*",
             "H": "****",
             "I": "**",
             "J": "*---",
             "K": "-*-",
             "L": "*-**",
             "M": "--",
             "N": "-*",
             "O": "---",
             "P": "*--*",
             "Q": "--*-",
             "R": "*-*",
             "S": "***",
             "T": "-",
             "U": "**-",
             "V": "***-",
             "W": "*--",
             "X": "-**-",
             "Y": "-*--",
             "Z": "--**",
             "1": "*----",
             "2": "**---",
             "3": "***--",
             "4": "****-",
             "5": "*****",
             "6": "-****",
             "7": "--***",
             "8": "---**",
             "9": "----*",
             "0": "-----"}

def generate_morse():
    userInput = input("Input a word: ").upper()
    wordlist = list(userInput)
    try:
        codelist = [morseDict[code] for code in wordlist]
    except KeyError:
        print("Please enter only letters and numbers")
        generate_morse()
    else:
        print(wordlist)
        print(codelist)


generate_morse()
