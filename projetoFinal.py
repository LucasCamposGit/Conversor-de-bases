import os
import funcoes
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

while True:
    print("opções: \n[1]tranformar decimal para outras bases \n[2]transformar outras bases em decimal \n[0]sair\n")
    escolha1 = int(input('digite a opção desejada: '))

    if escolha1 == 0:
        cls()
        print("Até logo")
        break

    elif escolha1 == 1:
        cls()
        print('Calculadora decimal para outras bases: ')
        print('[1] Decimal para binário \n[2] Decimal para hexadecimal \n[3] Decimal para octadecimal')
        opc = int(input('Digite uma opção: '))

        if opc == 1:
            funcoes.dec2bin(int(input("Digite o valor decimal: ")))  
        elif opc == 2:
            funcoes.dec2hex(int(input("Digite o valor decimal: "))) 
        elif opc == 3: 
            funcoes.dec2oct(int(input("Digite o valor decimal: "))) 

    elif escolha1 == 2:
        cls()
        print("calculadora para base 10 (decimal)")
        print('[1] binário para decimal   \n[2] Octal para decimal \n[3] Hexadecimal para decimal\n[0] Sair')
        opc = int(input('Digite uma opção: '))
        
        if opc == 1:
            funcoes.bin2dec(input("Digite o valor binario: "))  
        elif opc == 2:
            funcoes.oct2dec(input("Digite o valor octal: ")) 
        elif opc == 3: 
            funcoes.hex2dec(input("Digite o valor hexadecimal: ")) 
