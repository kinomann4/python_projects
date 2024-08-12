#You'll have to translate a string to Pilot's alphabet (NATO phonetic alphabet).

NATO = {
    'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta', 'E': 'Echo',
    'F': 'Foxtrot', 'G': 'Golf', 'H': 'Hotel', 'I': 'India', 'J': 'Juliett',
    'K': 'Kilo', 'L': 'Lima', 'M': 'Mike', 'N': 'November', 'O': 'Oscar',
    'P': 'Papa', 'Q': 'Quebec', 'R': 'Romeo', 'S': 'Sierra', 'T': 'Tango',
    'U': 'Uniform', 'V': 'Victor', 'W': 'Whiskey', 'X': 'X-ray', 'Y': 'Yankee', 'Z': 'Zulu'
}

def to_nato(words: str) -> str:
    result = []
    for char in words:
        if 65 <= ord(char) <= 90:  
            result.append(NATO[char])
        elif 97 <= ord(char) <= 122:  
            result.append(NATO[char.upper()])
        elif ord(char) == 32:
            pass
        else:
            result.append(char)
    return ' '.join(result)

print(to_nato("If, you can read?"))



