s = 'aA2'


if __name__ == '__main__':
    s = input()
    if len(s) > 0 and len(s) < 1000 :
        # any alphanumeric charachters
        print(any(char.isdigit() for char in s )  or any(char.isalpha() for char in s))

        # any alphabets
        print(any(char.isalpha() for char in s))

        # any digits
        print(any(char.isdigit() for char in s))

        # any lowercase alphabet
        print(any(char.islower() for char in s))
        
        # any uppercase alphabet
        print(any(char.isupper() for char in s))
        


