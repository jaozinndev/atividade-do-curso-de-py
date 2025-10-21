print("conversor de numeros.")
num = int(input("digite um numero inteiro para ser convertido:"))
print('''digite 1 se for para binario
digite 2 se for octal 
digite 3 se for hexadecimal''')
escolha = (int(input("sua escolha:--- ")))
if escolha == 1 :
    print(f'{num} em binario é igual a {bin(num)[2:]}')
elif escolha == 2 :
    print(f'{num} em octal ´é igual a {oct(num)[2:]} ')
elif escolha == 3 :
    print(f'{num} em hexadecimal é igual a {hex(num)[2:]}')
else :
    print('digite um numero inteiro. tente novamente')
