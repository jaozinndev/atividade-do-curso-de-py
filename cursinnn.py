print("bom dia vamos negociar seu emprestimo")
valor = float(input("quanto voce quer: "))
meses = float(input("digite a quantidade de tempo que voce quer pagar em anos : "))*12
salario = float(input("quanto voce ganha no mes: "))
prestacao = valor / meses
if prestacao >= salario * 30 / 100:
    print("a prestaçao é igual ou maior que trinta porcento do seu salario, nao podemos liberar o emprestimo.")
else:
    print(f"o emprestimo foi liberado, o valor a ser pago pelas parcelas sera de sera de {prestacao:.2f} tenha um otimo dia!!")
print("obrigado, volte sempre")