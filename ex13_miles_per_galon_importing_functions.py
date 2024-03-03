from random import randint

gallons = randint(10, 25)
miles = randint(200, 400)

mpg = miles // gallons

print("The car's fuel tank holds " + str(gallons) +" gallons of gas.")
print("The car can travel " + str(miles) + " miles on a full tank.")
print("The car's gas mileage (MPG) is " + str(mpg) + ".")

# używając f-stringów, nowy sposób wyświetlania danych różnego rodzaju bez potrzeby konwertowania danych liczbowych na stringi
gallons = randint(10, 25)
miles = randint(200, 400)

mpg = miles // gallons

print(f"The car's fuel tank holds {gallons} gallons of gas.")
print(f"The car can travel {miles} miles on a full tank.")
print(f"The car's gas mileage (MPG) is {mpg}.") 