#Leia uma temperatura em F e apresente ela em Cº
#formula  C = 5.0 * (F - 32.0)/9,0
F = float(input("Digite a temperatura em graus Fahrenheit: "))
C = (F - 32) * (5 / 9)

print("Valor em Celsius: ", C, "ºC")