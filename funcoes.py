def dec2bin(dec):
    bin = ''

    while dec != 0:
        r = dec % 2
        bin =  str(r) + bin 
        dec = dec // 2
    print(f'O valor em binário é de: {bin}')


def dec2hex(dec):
    dec1 = int(dec)
    hex = ''
    lista = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    while dec1 != 0:
        r = dec1 % 16
        hex = str(lista[r]) + hex
        dec1 = dec1 // 16

    print(f'O valor em hexadecimal é de: {hex}')
        
def dec2oct(dec):
    octa = ''

    while dec != 0:
        r = dec % 8
        octa =  str(r) + octa
        dec = dec // 8
    print(f'O valor em octadecimal é de: {octa}')

def hex2dec(hex):
    n = len(hex) 
    decimal = 0
    comt = 0
    
    for d in hex:
        if d == 'f':
            comt = 15
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1

        elif d == 'e':
            comt = 14
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1
        elif d == 'd':
            comt = 13
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1
        elif d == 'c':
            comt = 12
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1
        elif d == 'b':
            comt = 11
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1
        elif d == 'a':
            comt = 10
            decimal = decimal + comt * 16 ** (n-1)
            n = n - 1
        else:        
            decimal = decimal + int(d) * 16 ** (n-1)
            n = n - 1
    print(f'O valor em decimal é de: {decimal}')

def oct2dec(octa):
    n = len(octa) 
    decimal = 0

    for d in octa: 
        decimal = decimal + int(d) * 8 ** (n-1)
        n = n - 1
    print(decimal)
    
def bin2dec(bin):
    n = len(bin) 
    decimal = 0
    
    for d in bin: 
        decimal = decimal + int(d) * 2 ** (n-1)
        n = n - 1
    print(f'O valor em decimal é de: {decimal}')