numbers = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 15: 'fifteen', 18: 'eighteen',
    20: 'twenty', 30: 'thirty', 50: 'fifty', 80: 'eighty'
}

for i in range(14, 100):
    if i not in numbers:
        if i < 20:
            numbers[i] = f'{numbers[i - 10]}teen'
        elif 20 <= i < 40:
            numbers[i] = f'{numbers[i // 10 * 10]} {numbers[i % 10]}'
        elif 40 <= i < 50 or 60 <= i < 80 or 90 <= i < 100:
            numbers[i] = f'{numbers[i // 10]}ty {numbers[i % 10]}'
        elif 50 <= i < 60 or 80 <= i < 90:
            numbers[i] = f'{numbers[i // 10 * 10]} {numbers[i % 10]}'


def number_to_date(number):
    if number % 1000 == 0:
        return f'{numbers[int(str(number)[0:1])]} thousand'
    elif number % 100 == 0:
        return f'{numbers[int(str(number)[0:2])]} hundred'
    else:
        return f'{numbers[int(str(number)[0:2])]} {numbers[int(str(number)[2:4])]}'


assert number_to_date(2020) == 'twenty twenty'
assert number_to_date(1789) == 'seventeen eighty nine'
assert number_to_date(2000) == 'two thousand'
assert number_to_date(2100) == 'twenty one hundred'
