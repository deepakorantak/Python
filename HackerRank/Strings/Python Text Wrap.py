import textwrap

def wrap(string, max_width):
    output = ""
    if (len(string) > 0 and len(string) < 1000) and (max_width > 0 and max_width < len(string)):
        output = "\n".join(textwrap.wrap(string,max_width))

    return output

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)