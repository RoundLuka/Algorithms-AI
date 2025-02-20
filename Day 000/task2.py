"""2) დაწერეთ და გაუშვით პროგრამა, რომელსაც რიცხვები გადა-
ყავს ერთი პოზიციური სისტემიდან მეორეში ჩაშენებული ფუნ-
ქციების გამოყენების გარეშე. პროგრამა მინიმუმ უნდა მუშა-
ობდეს 2,4,10,16 ფუძის მქონე სისტემებისთვის."""

def position_convert(current_position, target_position, number):

    def manual_ord(char):
        my_ascii_table = {' ': 32, '!': 33, '"': 34, '#': 35, '$': 36, '%': 37, '&': 38, "'": 39, '(': 40, ')': 41, '*': 42, '+': 43, ',': 44, '-': 45, '.': 46, '/': 47, '0': 48, '1': 49, '2': 50, '3': 51, '4': 52, '5': 53, '6': 54, '7': 55, '8': 56, '9': 57, ':': 58, ';': 59, '<': 60, '=': 61, '>': 62, '?': 63, '@': 64, 'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70, 'G': 71, 'H': 72, 'I': 73, 'J': 74, 'K': 75, 'L': 76, 'M': 77, 'N': 78, 'O': 79, 'P': 80, 'Q': 81, 'R': 82, 'S': 83, 'T': 84, 'U': 85, 'V': 86, 'W': 87, 'X': 88, 'Y': 89, 'Z': 90, '[': 91, '\\': 92, ']': 93, '^': 94, '_': 95, '`': 96, 'a': 97, 'b': 98, 'c': 99, 'd': 100, 'e': 101, 'f': 102, 'g': 103, 'h': 104, 'i': 105, 'j': 106, 'k': 107, 'l': 108, 'm': 109, 'n': 110, 'o': 111, 'p': 112, 'q': 113, 'r': 114, 's': 115, 't': 116, 'u': 117, 'v': 118, 'w': 119, 'x': 120, 'y': 121, 'z': 122, '{': 123, '|': 124, '}': 125, '~': 126}
        return my_ascii_table[char]

    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

    def cast_int(num):
        result = 0
        for char in num:
            result += (result * 10) + (manual_ord(char) - manual_ord("0"))
        return result

    def manual_str(num):
        if num < 10:
            return str(num)
        elif 10 <= num < 36:
            return alphabet[num]
        elif 36 <= num < 62:
            return alphabet[num]

    def manual_len(number):
        length = 0
        for char in number:
            length += 1
        return length

    dec = 0
    i = 0
    length = manual_len(number)
    reversed_number = number[::-1]

    while i < length:
        digit = reversed_number[i]
        if cast_int(digit) > current_position - 1:
            return f"Invalid input {digit} isn't possible to be in {current_position} positional system"
        dec += cast_int(digit) * (current_position ** i)
        i += 1

    remainders = ""
    while dec > 0:
        remainders += manual_str(dec % target_position)
        dec //= target_position

    res = remainders[::-1]
    return cast_int(res)

print(position_convert(10, 16, "16"))
