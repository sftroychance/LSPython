# In this kata you have to write a simple Morse code decoder. Morse code is case-insensitive, traditionally capital letters are used. When the message is written in Morse code, a single space is used to separate the character codes and 3 spaces are used to separate words.

MORSE_CODE = {
    ".-": "A",
    "-...": "B",
    "-.-.": "C",
    "-..": "D",
    ".": "E",
    "..-.": "F",
    "--.": "G",
    "....": "H",
    "..": "I",
    ".---": "J",
    "-.-": "K",
    ".-..": "L",
    "--": "M",
    "-.": "N",
    "---": "O",
    ".--.": "P",
    "--.-": "Q",
    ".-.": "R",
    "...": "S",
    "-": "T",
    "..-": "U",
    "...-": "V",
    ".--": "W",
    "-..-": "X",
    "-.--": "Y",
    "--..": "Z",
    "-----": "0",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9"
}

def decode_morse(morse_code):
    # return ' '.join(
    #     ''.join(
    #         MORSE_CODE[letter] for letter in word.split()
    #     )
    #     for word in morse_code.strip().split('   ')
    # )

    result = ''

    for word in morse_code.strip().split('   '):
        result += ''.join([MORSE_CODE[letter] for letter in word.split()])
        result += ' '

    return result.strip()


print(decode_morse('.... . -.--   .--- ..- -.. .') == 'HEY JUDE')
