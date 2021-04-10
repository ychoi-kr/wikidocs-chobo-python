def korean_number(num):
    digits = {0: '영', 1: '일', 2: '이', 3: '삼', 4: '사', 5: '오', 6: '육', 7: '칠', 8: '팔', 9: '구'}
    d, m = divmod(num, 10)
    if 0 <= num < 10:
        return digits[m]
    elif num == 10:
        return '십'
    elif 10 < num < 20:
        return '십' + digits[m]
    elif 20 <= num < 100:
        _digits_copy = digits.copy()
        _digits_copy[0] = ''
        return digits[d] + '십' + _digits_copy[m]
    else:
        return '백'

