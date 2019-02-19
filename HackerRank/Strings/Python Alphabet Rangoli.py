import string
alpha = string.ascii_letters

size = int(input())

if size > 0 and size < 27:
    # all_chars = '-'.join([chr(i) for i in range(98,98+size-1)])
    # middle_line = all_chars[::-1] + '-a-' + all_chars
    line_length = size*2 + (size-1)*2 - 1
    lower_pattern = []
  
    for i in range(0,size):
         line = '-'.join(alpha[i:size])
         line = line[::-1] + line[1:]
         line = line.center(line_length,'-')
         lower_pattern.append(line)
    
    pattern = ('\n').join(lower_pattern[::-1] +  lower_pattern[1:])
    print(pattern)