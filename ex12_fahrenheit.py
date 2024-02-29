fah_temp = int(input("please input Fahrenheit temperature: "))


def fahrenheit(f):
    return round(1.8 * fah_temp + 32, 1)


print("The Fahrenheit equivalent of " + str(fah_temp) + " degrees Celsius is " + str(fahrenheit(fah_temp)))
