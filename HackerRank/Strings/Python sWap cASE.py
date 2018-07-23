def swap_case(s):
    return str.swapcase(s)

if __name__ == '__main__':
    s = input()
    if len(s) > 0 and len(s) <= 1000:
        result = swap_case(s)
        print(result)