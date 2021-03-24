def palindrome(s):
    s = s.lower()
    s = s.replace(' ', '')
    return s[:] == s[::-1]

if __name__ == '__main__':
    for x in ['anna', 'banana', 'Anna', 'My gym']:
        if palindrome(x):
            print(f"'{x}' is a panlindrome")
        else:
            print(f"'{x}' is not a palindrome")
