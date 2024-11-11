substitution = {
    "a": "f",
    "b": "g",
    "c": "h",
    "d": "i",
    "e": "j",
    "f": "k",
    "g": "l",
    "h": "m",
    "i": "n",
    "j": "o",
    "k": "p",
    "l": "q",
    "m": "r",
    "n": "s",
    "o": "t",
    "p": "u",
    "q": "v",
    "r": "w",
    "s": "x",
    "t": "y",
    "u": "z",
    "v": "a",
    "w": "b",
    "x": "c",
    "y": "d",
    "z": "e"
}

message = input("Please enter your message:").lower()

coded_message = ""
for char in message:
    if char in substitution:
        char = substitution[char]
    coded_message += char

print(coded_message)
