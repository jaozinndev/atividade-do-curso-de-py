idade = 2025 - (int(input("que ano voce nasceu ?")))
if idade == 18 :
    print(f"em 2025 voce tem {idade} anos\n aliste-se IMEDIATAMENTE!!!")
elif idade < 18 :
    tp = 18 - idade
    print(f"ainda há tempo, em 2025 voce tem {idade} anos,  falta {tp} anos para se ingressar.")
else :
    tp = idade - 18
    print(f"em 2025 voce tem {idade} anos, ja passou {tp} anos do ano de se alistar, VÁ LOGO!!")