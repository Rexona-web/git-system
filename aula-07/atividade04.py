peso = float(input("Digite seu peso: "))
altura = float(input("Qual sua altura: "))

imc = peso / (altura ** altura) 
print("Seu IMC é: ", imc)

if imc >=30: 
    print("obesidade")
elif imc >=25:
    print ("Sobrepeso")
elif imc >=18.5:
    print("Peso ideal")
else:
    print("Abaixo do peso")