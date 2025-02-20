"""1) მოცემული 3 მთელი a,b,c̸=0რიცხვებისთვის მოძებნეთ aდა
bრიცხვებს შორის მოხვედრილი c რიცხვის ჯერადი რიცხვების
რაოდენობა ყველა შესაძლო ვარიანტისთვის. თუ რომელიმე
a,b-დან ჯერადია c-ს, მაშინ ჩათვალეთ შესაბამისი საზღვარი.
მოიფიქრეთ ამოცანის ამოხსნის ალგორითმი, დაწერეთ და გა-
უშვით პროგრამა ციკლის და რეკურსიის (აგრეთვე range) კონ-
სტრუქციის გამოყენების გარეშე."""


def find_max(a, b, c):
    if a > b:
        if b % c == 0:
            start = b
        else:
            start = b - (b % c)
        if a % c == 0:
            end = a
        else:
            end = a - (a % c)
    else:
        if a % c == 0:
            start = a
        else:
            start = a + (c - (a % c))
        if b % c == 0:
            end = b
        else:
            end = b - (b % c)
    if start > end:
        return 0
    return ((end - start) // c) + 1

print(find_max(3, 14, 3))  # Output: 4 (3, 6, 9, 12)
print(find_max(14, 3, 3))  # Output: 4 (3, 6, 9, 12)
print(find_max(3, 14, 5))  # Output: 3 (5, 10)
print(find_max(3, 14, 7))  # Output: 2 (7, 14)
print(find_max(1, 10, 2))  # Output: 5 (2, 4, 6, 8, 10)