numbers = {
    0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
    10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 15: 'fifteen', 18: 'eighteen',
    20: 'twenty', 30: 'thirty', 50: 'fifty'
}

for i in range(14, 100):
    if i not in numbers:
        if i < 20:
            numbers[i] = f'{numbers[i - 10]}teen'
        elif 20 <= i < 40:
            numbers[i] = f'{numbers[i // 10 * 10]} {numbers[i - (i // 10 * 10)]}'
        elif 40 <= i < 50 or 60 <= i < 80 or 90 <= i < 100:
            numbers[i] = f'{numbers[i // 10]}ty {numbers[i % 10]}'
        elif 50 <= i < 60:
            numbers[i] = f'{numbers[50]} {numbers[i % 10]}'
        elif 80 <= i < 90:
            numbers[i] = f'{numbers[8]}y {numbers[i % 10]}'


def number_to_date(number):
    return f'{numbers[int(str(number)[0:2])]} {numbers[int(str(number)[2:4])]}'


assert number_to_date(2020) == 'twenty twenty'
assert number_to_date(1789) == 'seventeen eighty nine'
