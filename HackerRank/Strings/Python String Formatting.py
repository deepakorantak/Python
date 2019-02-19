from decimal import Decimal 
n = int(input())
no_repeat = len('{0:b}'.format(n))
print(no_repeat)
if n >= 1 and n <= 99:
    print('\n'.join([ '{0:{width}d}'.format(i,width=no_repeat) +
                      '{0:{width}o}'.format(i,width=no_repeat+1) +
                      '{0:{width}X}'.format(i,width=no_repeat+1) +
                      '{0:{width}b}'.format(i,width=no_repeat+1)
                         for i in range(1,n+1)]))
                        