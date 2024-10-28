with open('data.txt') as f:
    data = f.read()
    data = data.split('\n')
    data.pop()

digits = ['1','2','3','4','5','6','7','8','9']
words = ['one','two','three','four','five','six','seven','eight','nine']
def word_to_digit(word):

    match word:
        case 'one':
            return '1'
        case 'two':
            return '2'
        case 'three':
            return '3'
        case 'four':
            return '4'
        case 'five':
            return '5'
        case 'six':
            return '6'
        case 'seven':
            return '7'
        case 'eight':
            return '8'
        case 'nine':
            return '9'


total = 0


for i in range(len(data)):
    first_digit = ''
    second_digit = ''
    value = ''
    word = ''
    for char in data[i]:
        if char in digits:
            second_digit = char
            word = ''
            if not first_digit:
                first_digit = char
        else:
            word += char
            matches = False
            for item in words:
                if word == item:
                    second_digit = word_to_digit(word)
                    word = ''
                    if not first_digit:
                        first_digit = second_digit
                if word in item:
                    matches = True
            if not matches:
                word = word[1:]

    value = first_digit + second_digit
    print(f'{data[i]}: {value}')
    total += int(value)

print(total)